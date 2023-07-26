import asyncio

import requests
from celery import Celery
from celery.schedules import crontab
from sqlalchemy import select

from core.database.database import redis_connection, Async_session, redis_uri
from core.database.models import Cargo


celery = Celery('tasks', broker=redis_uri)
celery.conf.beat_schedule = {
    'calculate_delivery_cost': {
        'task': 'tasks.calculate_delivery_cost',
        'schedule': crontab(minute='*/5'),
    },
}

@celery.task
async def calculate_delivery_cost():
    try:
        usd_exchange_rate = redis_connection.get('usd')
        db_connection = Async_session()
        cargos_query = select(Cargo).filter(Cargo.delivery_cost == None)
        cargos_without_delivery_cost = await db_connection.execute(cargos_query)
        cargos_without_delivery_cost = cargos_without_delivery_cost.scalars().all()
        for _ in cargos_without_delivery_cost:
            delivery_cost = (_.weight * 0.5 + _.cargo_cost * 0.01) * usd_exchange_rate
            _.delivery_cost = delivery_cost
            await db_connection.commit()
    except Exception as e:
        get_usd_exchange_rate()
        await calculate_delivery_cost()


def get_usd_exchange_rate():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    return redis_connection.set('USD', response.json()['Valute']['USD']['Value'], keepttl=600)

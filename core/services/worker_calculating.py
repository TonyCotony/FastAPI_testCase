"""
Создал воркер без использования celery, для простоты понимания структуры проекта и без нагромождений
При дальнейшем развитии, по-моему мнению нужно выносить воркеры в отдельный проект
со своей инфраструктурой, поэтому не смог придумать адекватное место куда его 'определить'
"""
import asyncio
import aiohttp

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.database_session import get_db_session, get_redis_connection
from core.database.models import Cargo
from core.loggs.logger import logger
from core.sessions.rabbitMQ_session import get_channel
from settings import settings


# from core.sessions.rabbitMQ_session import channel, delivery_calculating_queue


def callback(ch, method, properties, body):
    cargo_id = int(body.decode())
    asyncio.run(calculate_n_update_delivery_cost(cargo_id))  # , db_session))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


async def calculate_n_update_delivery_cost(cargo_id) -> None:
    db_session = await get_db_session()
    cargo = await get_cargo_by_id(cargo_id, db_session)
    delivery_cost = await calculate_delivery_cost(cargo)
    cargo.delivery_cost = delivery_cost
    await db_session.commit()
    await db_session.close()


async def get_cargo_by_id(cargo_id: int, db_session: AsyncSession):
    """достает данные о грузе из ДБ, для рассчета доставки"""
    # db_session = await get_db_session()
    query = select(Cargo).filter(Cargo.id == cargo_id)
    cargo = await db_session.execute(query)

    cargo = cargo.scalars().first()

    return cargo


async def calculate_delivery_cost(cargo: Cargo) -> float:
    usd_currency = await get_usd_currency()
    weight = cargo.weight
    cargo_cost = cargo.cargo_cost
    delivery_cost = (weight * 0.5 + cargo_cost * 0.01) * usd_currency
    return delivery_cost


async def get_usd_currency() -> float:
    """запрос к redis для получения кешированного курса, елси подключение установить не удается,
    то делаем запрос к сайту из ТЗ и возвращаем курс"""
    try:
        redis_connection = get_redis_connection()
    except Exception as e:
        print(e)
        return await queue_for_usd_currency()

    try:
        usd_currency = redis_connection.get('usd')
    except Exception as e:
        print(f'get currency error with redis - {e}')
        usd_currency = None
    finally:
        # Если значение не найдено изза ттл, или проблемы с редис, обновляем курс через запрос
        if usd_currency is None:
            print('update currency')
            usd_currency = await update_usd_currency(redis_connection)
    return float(usd_currency)


async def queue_for_usd_currency():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                usd_currency = await response.json(content_type=None)
                usd_currency = usd_currency['Valute']['USD']['Value']

                return usd_currency
        except Exception as e:
            print(f"update currency error - {e}")
            await asyncio.sleep(2)
            await queue_for_usd_currency()


async def update_usd_currency(redis_connection) -> float:
    """Делаем запрос к сайту из ТЗ и пытаемся обновить курс в Redis.
    Если с подключением к Redis что-то не так, просто возвращаем курс, не обновляя в редис"""
    usd_currency = await queue_for_usd_currency()
    try:
        redis_connection.set('usd', usd_currency, keepttl=600)
        print(f'this is usd currency - {usd_currency}')
        return usd_currency

    except Exception as e:
        print(f"update currency error - {e}")
        return usd_currency


logger.info('calculating worker started')
channel = get_channel(
    exchange_name=settings.rabbitMQ.exchange_name,
    queue_name=settings.rabbitMQ.queue_calculate,
    routing_key=settings.rabbitMQ.routing_key_calculate
)
channel.basic_consume(queue=settings.rabbitMQ.queue_calculate, on_message_callback=callback)

channel.start_consuming()

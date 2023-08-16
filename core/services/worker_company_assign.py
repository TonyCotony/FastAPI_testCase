"""
Создал воркер без использования celery, для простоты понимания структуры проекта и без нагромождений
При дальнейшем развитии, по-моему мнению нужно выносить воркеры в отдельный проект
со своей инфраструктурой, поэтому не смог придумать адекватное место куда его 'определить'
"""
import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.database_session import get_db_session
from core.database.models import Cargo, Company
from core.loggs.logger import logger
from core.sessions.rabbitMQ_session import get_channel
from settings import settings


def callback(ch, method, properties, body):
    cargo_id = str(body.decode()).split('|')
    company_id = int(cargo_id[1])
    cargo_id = int(cargo_id[0])
    print(f'{cargo_id}    -     {company_id}')
    print(f'{type(cargo_id)}      -      {type(company_id)}')
    asyncio.run(check_availability_assign_delivery_company(cargo_id=cargo_id, company_id=company_id))
    ch.basic_ack(delivery_tag=method.delivery_tag)


async def check_availability_assign_delivery_company(cargo_id: int, company_id: int):
    """на случай возможного пропуска задачи, или неработоспособности сервисов в процессе обмена сообщениями"""
    db_session = await get_db_session()
    # query = select(Cargo).filter(Cargo.id == cargo_id)
    # cargo = await db_session.execute(query)
    # cargo = cargo.scalars().first()
    cargo = await get_cargo_by_id(cargo_id=cargo_id, db_session=db_session)
    if cargo.delivery_company is None:
        await assign_deliver_company_to_cargo(cargo, company_id, db_session)
        message = (f'CONGRATULATIONS!!! We confirm that you will deliver the cargo with id - {cargo_id}'
                   f'\nAnd name - {cargo.name}'
                   f'\nDelivery price is - {cargo.delivery_cost}')
    else:
        message = f'We apologize, a representative from another company has secured this сфкпщ prior to you'
    query = select(Company).filter(Company.id == company_id)
    company_email = await db_session.execute(query)
    company_email = company_email.scalars().first()
    company_email = company_email.email
    return await send_email(message, company_email)


async def assign_deliver_company_to_cargo(cargo: Cargo, company_id: int, db_session: AsyncSession):
    cargo.delivery_company = company_id
    await db_session.commit()
    await db_session.close()


async def send_email(message: str, email: str):
    """Здесь будет функция настроенная на отправку сообщений, например с использованием celery,
    либо связка celery + rabbitmq, в ТЗ об этом не было, я лишь описываю как я вижу эту реализацию,
    учитывая крайне малый опыт взаимодейтсвия с rabbitmq"""
    print(f'Email will be send to {email} with next message:\n\n{message}')
    pass


async def get_cargo_by_id(cargo_id: int, db_session: AsyncSession):
    """достает данные о грузе из ДБ, для рассчета доставки"""
    # db_session = await get_db_session()
    print(cargo_id)
    query = select(Cargo).filter(Cargo.id == cargo_id)
    print(query)
    cargo = await db_session.execute(query)

    cargo = cargo.scalars().first()

    return cargo


logger.info('calculating worker started')
channel = get_channel(
    exchange_name=settings.rabbitMQ.exchange_name,
    queue_name=settings.rabbitMQ.queue_company_assign,
    routing_key=settings.rabbitMQ.routing_key_company_assign
)
channel.basic_consume(queue=settings.rabbitMQ.queue_company_assign, on_message_callback=callback)

channel.start_consuming()

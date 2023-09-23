import asyncio
import random
import socket
import time

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
#
# from core.database.database_session import redis_local, redis_connection, get_db_session
# from core.database.models import Company, Cargo
#
# x = socket.getaddrinfo(redis_local, 6379)
# print(x)
#
# data = redis_connection.get('usd')
# print(data)
# print(type(data))
# print(float(data))
# print(type(float(data)))
#
#
# def get_data_from_db(some_id):
#     info = asyncio.run(start_async_get(some_id))
#     print(info.name)
#     return info
#
#
# async def start_async_get(some_id):
#     connect = await get_db_session()
#     info = await get_some_info(some_id, connect)
#     print(info.delivery_cost)
#     return info
#
#
# async def get_some_info(some_id: int, session: AsyncSession):
#     query = select(Cargo).filter(Cargo.id == some_id)
#     info = await session.execute(query)
#     await session.close()
#     info = info.scalars().first()
#     return info
#
# a = get_data_from_db(random.randint(1,20))
# print(a.cargo_cost)
#
#
# def callback(cargo_id, company_id):
#     # cargo_id = str(body.decode()).split('|')
#     # company_id = int(cargo_id[1])
#     # cargo_id = int(cargo_id[0])
#     print(f'{cargo_id}    -     {company_id}')
#     asyncio.run(check_availability_assign_delivery_company(cargo_id, company_id))
#     # ch.basic_ack(delivery_tag=method.delivery_tag)
#
#
# async def check_availability_assign_delivery_company(cargo_id: int, company_id: int):
#     """на случай возможного пропуска задачи, или неработоспособности сервисов в процессе обмена сообщениями"""
#     db_session = await get_db_session()
#     # query = select(Cargo).filter(Cargo.id == cargo_id)
#     # cargo = await db_session.execute(query)
#     # cargo = cargo.scalars().first()
#     cargo = await get_cargo_by_id(cargo_id, db_session)
#
#
# async def get_cargo_by_id(cargo_id: int, db_session: AsyncSession):
#     """достает данные о грузе из ДБ, для рассчета доставки"""
#     # db_session = await get_db_session()
#     print(cargo_id)
#     query = select(Cargo).filter(Cargo.id == cargo_id)
#     print(query)
#     cargo = await db_session.execute(query)
#
#     cargo = cargo.scalars().first()
#     print(cargo.name, ' ', cargo.weight)
#     return cargo
#
#
# callback(random.randint(1,20), random.randint(1,3))


def get_try(a: list):
    try:
        print(a[10])
    except Exception as e:
        print(e)
        time.sleep(2)
        a += [1]
        return get_try(a)
    print(f"done {a}")

a = get_try([])

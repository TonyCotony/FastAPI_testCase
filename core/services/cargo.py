from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.models import Cargo, CargoType, UserSession
from core.dto.cargo import CargoType as CargoTypeDTO, DeliveryData
from core.dto.cargo import CargoTypes as CargoTypesDTO
from core.dto.cargo import ShowCargo, CargoWithoutDeliveryPrice, CargoBase, Cargos, CargoFilter, CargoId
from core.sessions.rabbitMQ_session import get_channel, property_for_calculating_n_assign
from core.loggs.logger import logger
from settings import settings


async def register_cargo(
        data: CargoBase,
        db_session: AsyncSession,
        session_id: UUID
) -> CargoWithoutDeliveryPrice or Exception:
    session_id = await get_user_session_id(db_session, session_id)

    # Немного изменил логику реализации. набор данных попадает сразу в БД, чтобы без ожидания выдать клиенту ID посылки
    # и сразу же в очередь rmq отправляется задача воркеру на просчет стоимости доставки
    # Да получаются два дополнительных обращения к базе, по одному select & update, но по моим убеждениям клиенту
    # важенее получить уведомление о регистрации посылки быстрее, а потом(например в приложении) уже подгрузить данные
    # о стоимости доставки
    # понимаю, что в этом из-за временной неработоспообности сервисов может быть пропущенна стоимость доставки,
    # можно сделать через селери задачу по времени. это мой первый проект на FastAPI и RabbitMQ, поэтому я не смогу их
    # подружить в сжатый срок
    new_cargo = Cargo(
        name=data.name,
        weight=data.weight,
        type=data.type,
        cargo_cost=data.cargo_cost,
        delivery_cost=None,
        session_id=session_id
    )

    try:
        db_session.add(new_cargo)
        await db_session.commit()
        await db_session.refresh(new_cargo)

    except Exception as e:
        logger.warning(f'Error with adding new cargo - {e}')
        return e

    send_register_cargo_data_to_rabbit(new_cargo.id)

    return CargoWithoutDeliveryPrice(
        id=new_cargo.id,
        name=new_cargo.name,
        weight=new_cargo.weight,
        type=new_cargo.type,
        cargo_cost=new_cargo.cargo_cost,
    )


async def get_cargo(cargo_id: CargoId, db_session: AsyncSession) -> ShowCargo or CargoWithoutDeliveryPrice or str:
    """Возвращает груз с выбранным id"""
    try:
        query = select(Cargo).filter(Cargo.id == cargo_id.id)
        result = await db_session.execute(query)
        result = result.scalars().first()
    except Exception as e:
        logger.warning(f'Trouble with find cargo - {e}')
        return 'trouble with DB'

    if result is not None:
        return ShowCargo(
            id=result.id,
            name=result.name,
            weight=result.weight,
            type=result.type,
            cargo_cost=result.cargo_cost,
            delivery_cost=result.delivery_cost,
            session_id=result.session_id
        )
    else:
        return "we haven't cargo with this id"


async def get_owned_cargo(db_session: AsyncSession,
                          session_id: UUID, filter_data: CargoFilter) -> ShowCargo or CargoWithoutDeliveryPrice or str:
    """Возвращает все грузы относящиеся к сессии с учетом фильтрации и пагинации"""
    query = select(Cargo)

    # Фильтрация по типу посылки
    if filter_data.cargo_type is not None:
        if isinstance(filter_data.cargo_type, int):
            query = query.filter(Cargo.type == filter_data.cargo_type)
        elif isinstance(filter_data.cargo_type, list):
            for _ in filter_data.cargo_type:
                query = query.filter(Cargo.type == filter_data.cargo_type)

    # Фильтрация по наличию рассчитанной стоимости доставки
    if filter_data.delivery_cost_calculated is not None:
        if filter_data.delivery_cost_calculated is False:
            query = query.filter(Cargo.delivery_cost is None)
        else:
            query.filter(Cargo.delivery_cost is not None)

    # Пaгинация
    try:
        session_id = await get_user_session_id(db_session, session_id)
        query = query.filter(Cargo.session_id == session_id)
        skip = (filter_data.page - 1) * filter_data.per_page
        query = query.offset(skip).limit(filter_data.per_page)
        filtered_data = await db_session.execute(query)
        filtered_data = filtered_data.scalars().all()
    except Exception as e:
        logger.warning(f'Trouble with filtered cargo - {e}')
        return 'Trouble with DB'

    if len(filtered_data) > 0:
        formatted_cargos = [serialize_cargo_n_delivery_cost(cargo) for cargo in filtered_data]
        return Cargos(cargos=formatted_cargos)
    else:
        return "u haven't any cargos or cargos by your filter(s)"


def serialize_cargo_n_delivery_cost(cargo: ShowCargo) -> ShowCargo:
    """Эта функция принудительно сериализует модель Cargo в pydantic ShowCargo"""
    return ShowCargo(
        id=cargo.id,
        name=cargo.name,
        weight=cargo.weight,
        type=cargo.type,
        cargo_cost=cargo.cargo_cost,
        session_id=cargo.session_id,
        delivery_cost=cargo.delivery_cost
    )


async def get_cargo_types(db_session: AsyncSession) -> CargoTypesDTO or str:
    """Достает с базы и сериализует данные для возврата"""
    query = select(CargoType)
    try:
        result = await db_session.execute(query)
    except Exception as e:
        logger.warning(f'Trouble with get type of cargo - {e}')
        return 'trouble with DB'

    result = result.scalars().all()
    serialized_cargo_types = [serialize_cargo_types(cargo_type) for cargo_type in result]
    return CargoTypesDTO(
        cargo_types=serialized_cargo_types
    )


def serialize_cargo_types(cargo_type: CargoType) -> CargoTypeDTO:
    """сериализует данные типов грузов"""
    return CargoTypeDTO(
        id=cargo_type.id,
        name=cargo_type.name
    )


async def get_user_session_id(db_session: AsyncSession, session_id: UUID) -> int:
    """достает id пользовательской сессии по ее uuid"""

    query = select(UserSession.id).where(UserSession.session_id == str(session_id))
    try:
        user_session_id = await db_session.execute(query)
    except Exception as e:
        logger.warning(f'Trouble with find cargo - {e}')
        return await get_user_session_id(db_session, session_id)

    user_session_id = user_session_id.scalars().first()
    return user_session_id


def send_register_cargo_data_to_rabbit(cargo_id: int) -> None:
    """Отправляем ID груза в rabbitMQ, для рассчета его стоимости"""

    # изменить все временные данные, сохранить их в сеттингс/инпут
    exchange_name = settings.rabbitMQ.exchange_name
    routing_key = settings.rabbitMQ.routing_key_calculate
    channel = get_channel(
        exchange_name=exchange_name,
        queue_name=settings.rabbitMQ.queue_calculate,
        routing_key=routing_key
    )
    try:
        channel.basic_publish(

            exchange=exchange_name,
            routing_key=routing_key,
            body=str(cargo_id),
            properties=property_for_calculating_n_assign,
            mandatory=True,
        )
    except Exception as e:
        # для надежности и стабильности, нужен асинхронный коннект к рэббит
        # чтобы не вешать приложение бесконечной отправкой скриптов или не асинхроным ожиданием
        # для упрощения разработки тестового выбран вариант синхронный
        logger.warning(f'Ошибка отправки сообщения в rabbit - {e}')
        return send_register_cargo_data_to_rabbit(cargo_id)


async def check_availability_cargo_delivery(data: DeliveryData, db_session: AsyncSession) -> str:
    """Сделал для ускорения разработки, запрос к БД, где явно проверяется наличие закрепленной компании, если таковой нет
    для гарантированного статуса получения запроса одной компанией, отправляем сообщение в rabbitmq"""
    query = select(Cargo.delivery_company).filter(Cargo.id == data.id)
    try:
        check = await db_session.execute(query)
    except Exception as e:
        logger.warning(f'Ошибка отправки сообщения в rabbit - {e}')
        return check_availability_cargo_delivery(data, db_session)

    check = check.scalars().first()
    if check is None:
        send_company_data_for_assign(data)
        return 'you will receive assign status by you company email'
    else:
        return 'This cargo is already been assigned by another delivery company'


def send_company_data_for_assign(data: DeliveryData) -> None:
    """отправляет сообщение в rabbit, для дальнейшей проверки возможности закрепления посылки за службой доставки"""
    exchange_name = settings.rabbitMQ.exchange_name
    routing_key = settings.rabbitMQ.routing_key_company_assign
    channel = get_channel(
        exchange_name=exchange_name,
        queue_name=settings.rabbitMQ.queue_company_assign,
        routing_key=routing_key
    )

    try:
        channel.basic_publish(

            exchange=exchange_name,
            routing_key=routing_key,
            body=str(f"{data.id}|{data.company_id}"),
            properties=property_for_calculating_n_assign,
            mandatory=True,
        )
    except Exception as e:
        # для надежности и стабильности, нужен асинхронный коннект к рэббит
        # чтобы не вешать приложение бесконечной отправкой скриптов или не асинхроным ожиданием
        # для упрощения выбран вариант синхронный
        logger.warning(f'Ошибка отправки сообщения в rabbit - {e}')
        return send_company_data_for_assign(data)

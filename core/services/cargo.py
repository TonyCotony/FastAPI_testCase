import math
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.models import Cargo, CargoType, UserSession, cargo_type
from core.dto.cargo import ShowCargo, CargoWithoutDeliveryPrice, CargoBase, Cargos, CargoFilter
from core.dto.cargo import CargoTypes as CargoTypesDTO
from core.dto.cargo import CargoType as CargoTypeDTO


async def register_cargo(data: CargoBase, db_session: AsyncSession, session_id: UUID) -> CargoWithoutDeliveryPrice:
    session_id = await get_user_session_id(db_session, session_id)

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
        print(e)

    return CargoWithoutDeliveryPrice(
        id=new_cargo.id,
        name=new_cargo.name,
        weight=new_cargo.weight,
        type=new_cargo.type,
        cargo_cost=new_cargo.cargo_cost,
    )


async def get_cargo(id: int, db_session: AsyncSession) -> ShowCargo or CargoWithoutDeliveryPrice or str:
    """возвращает груз с выбранным id"""
    query = select(Cargo).filter(Cargo.id == id)
    result = await db_session.execute(query)
    result = result.scalars().first()
    if result is not None:
        if isinstance(result.delivery_cost, float):
            return ShowCargo(
                id=result.id,
                name=result.name,
                weight=result.weight,
                type=result.type,
                cargo_cost=result.cargo_cost,
                delivery_cost=result.delivery_cost,
            )
        else:
            return CargoWithoutDeliveryPrice(
                id=result.id,
                name=result.name,
                weight=result.weight,
                type=result.type,
                cargo_cost=result.cargo_cost,
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

    # Пгинация
    session_id = await get_user_session_id(db_session, session_id)
    query = query.filter(Cargo.session_id == session_id)
    skip = (filter_data.page - 1) * filter_data.per_page
    query = query.offset(skip).limit(filter_data.per_page)
    filtered_data = await db_session.execute(query)
    filtered_data = filtered_data.scalars().all()

    if len(filtered_data) > 0:
        formatted_cargos = [serialize_cargo_n_delivery_cost(cargo) for cargo in filtered_data]
        return Cargos(cargos=formatted_cargos)
    else:
        return "u haven't any cargos or cargos by your filter(s)"


def serialize_cargo_n_delivery_cost(cargo: ShowCargo) -> ShowCargo:
    """необходимо было заменять None на "Не рассчитан", плюс были проблемы с сериализацией данных
    Эта функция принудительно сериализует модель Cargo в pydantic ShowCargo"""
    # Заменяем None на "Не рассчитан", если значение равно None
    if cargo.delivery_cost is None:
        cargo.delivery_cost = "Не рассчитан"
    return ShowCargo(
        id=cargo.id,
        name=cargo.name,
        weight=cargo.weight,
        type=cargo.type,
        cargo_cost=cargo.cargo_cost,
        session_id=cargo.session_id,
        delivery_cost=cargo.delivery_cost
    )


async def get_cargo_types(db_session: AsyncSession) -> CargoTypesDTO:
    """достает с базы и сериализует данные для возврата"""
    query = select(CargoType)
    result = await db_session.execute(query)

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


# async def get_cargo_filter(filter_data: CargoFilter, db_session: AsyncSession) -> Cargos:
#     """Применяет все фильтры к запросу, затем возвращает сериализованные данные"""
#     query = select(Cargo)
#
#     # Фильтрация по типу посылки
#     if filter_data.cargo_type is not None:
#         if isinstance(filter_data.cargo_type, int):
#             query = query.filter(Cargo.type == filter_data.cargo_type)
#         elif isinstance(filter_data.cargo_type, list):
#             for _ in filter_data.cargo_type:
#                 query = query.filter(Cargo.type == filter_data.cargo_type)
#
#     # Фильтрация по наличию рассчитанной стоимости доставки
#     if filter_data.delivery_cost_calculated is not None:
#         if filter_data.delivery_cost_calculated is False:
#             query = query.filter(Cargo.delivery_cost is None)
#         else:
#             query.filter(Cargo.delivery_cost is not None)
#
#     # Пгинация
#     skip = (filter_data.page - 1) * filter_data.per_page
#     query = query.offset(skip).limit(filter_data.per_page)
#     filtered_data = await db_session.execute(query)
#     filtered_data = filtered_data.scalars().all()
#     formatted_cargos = [serialize_cargo_n_delivery_cost(cargo) for cargo in filtered_data]
#
#     return Cargos(cargos=formatted_cargos)


async def get_user_session_id(db_session: AsyncSession, session_id: UUID) -> int:
    """достает id пользовательской сессии по ее uuid"""
    session_id = select(UserSession.id).where(UserSession.session_id == str(session_id))
    session_id = await db_session.execute(session_id)
    session_id = session_id.scalars().first()
    return session_id

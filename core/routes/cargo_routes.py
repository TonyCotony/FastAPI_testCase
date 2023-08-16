from uuid import uuid4, UUID

from fastapi import Depends, Response, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.database_session import get_db
from core.dto.cargo import CargoWithoutDeliveryPrice, CargoBase, CargoFilter, CargoId, DeliveryData
from core.services.user_session import add_session_to_db

from core.sessions.UUID_session import SessionData, backend, cookie
from core.services import cargo as cargo_services


router = APIRouter(
    prefix='',
    tags=['delivery']
)


@router.post("/create_session/{name}")
async def create_session(name: str, response: Response, db_session: AsyncSession = Depends(get_db)):
    """использовал этот роут, т.к. изначально видел приложение как часть большего сервиса, где авторизацией управляет
    другое приложение. Поэтому в него нельзя зайти в нашем случае без имеющейся сессии, которую мы регаем здесь"""
    session = uuid4()
    data = SessionData(username=name)

    await backend.create(session, data)
    cookie.attach_to_response(response, session)

    return await add_session_to_db(
        user_session=str(session),
        name=data.username,
        db_session=db_session
    )


@router.post('/register_cargo')
async def register_cargo(
        cargo_data: CargoBase,
        session_id: UUID = Depends(cookie),
        db_session: AsyncSession = Depends(get_db)
) -> CargoWithoutDeliveryPrice:
    return await cargo_services.register_cargo(cargo_data, db_session, session_id)


@router.get('/get_cargo')  # , dependencies=[Depends(cookie)])
async def get_cargo(cargo_id: CargoId, db_session: AsyncSession = Depends(get_db)):
    # не понятно, можно ли получать данные о посылке только по id или нужна еще и сессия
    # поэтому сделал без куки, но примеры с ними ниже
    return await cargo_services.get_cargo(cargo_id, db_session)


@router.get('/get_owned_cargos', dependencies=[Depends(cookie)])
async def get_owned_cargos(filter_data: CargoFilter, session_id: UUID = Depends(cookie),
                           db_session: AsyncSession = Depends(get_db)):
    return await cargo_services.get_owned_cargo(db_session, session_id, filter_data)


@router.get('/get_cargo_types')
async def get_cargo_types(db_session: AsyncSession = Depends(get_db)):
    return await cargo_services.get_cargo_types(db_session)


@router.post('/register_delivery')
async def register_delivery(delivery_data: DeliveryData, db_session: AsyncSession = Depends(get_db)):
    return await cargo_services.check_availability_cargo_delivery(delivery_data, db_session)

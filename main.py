import asyncio
from uuid import uuid4, UUID

import uvicorn
from fastapi import FastAPI, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.database import get_db
from core.dto.cargo import CargoWithoutDeliveryPrice, CargoBase, CargoFilter
from core.services.user_session import add_session_to_db

from core.sessions.session import SessionData, backend, verifier, cookie
from core.services import cargo as cargo_services

app = FastAPI()


@app.post("/create_session/{name}")
async def create_session(name: str, response: Response, db_session: AsyncSession = Depends(get_db)):
    session = uuid4()
    data = SessionData(username=name)

    await backend.create(session, data)
    cookie.attach_to_response(response, session)

    return await add_session_to_db(
        user_session=str(session),
        name=data.username,
        db_session=db_session
    )


@app.post("/delete_session")
async def del_session(response: Response, session_id: UUID = Depends(cookie)):
    await backend.delete(session_id)
    cookie.delete_from_response(response)
    return "deleted session"


@app.get("/whoami", dependencies=[Depends(cookie)])
async def whoami(session_data: SessionData = Depends(verifier)):
    return session_data


@app.post('/register_cargo', dependencies=[Depends(cookie)])
async def register_cargo(
        cargo_data: CargoBase,
        session_id: UUID = Depends(cookie),
        db_session: AsyncSession = Depends(get_db)
) -> CargoWithoutDeliveryPrice:
    return await cargo_services.register_cargo(cargo_data, db_session, session_id)


@app.get('/get_cargo', dependencies=[Depends(cookie)])
async def get_cargo(id: int, db_session: AsyncSession = Depends(get_db)):
    return await cargo_services.get_cargo(id, db_session)


@app.get('/get_owned_cargos', dependencies=[Depends(cookie)])
async def get_owned_cargos(filter_data: CargoFilter, session_id: UUID = Depends(cookie),
                           db_session: AsyncSession = Depends(get_db)):
    return await cargo_services.get_owned_cargo(db_session, session_id, filter_data)


@app.get('/get_cargo_types')
async def get_cargo_types(db_session: AsyncSession = Depends(get_db)):
    return await cargo_services.get_cargo_types(db_session)


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=8080,
        reload=True,
    )


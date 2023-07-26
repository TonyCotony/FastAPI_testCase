from uuid import uuid4

from core.database.models import UserSession


async def add_session_to_db(user_session: uuid4, name: str, db_session) -> str:
    new_session = UserSession(session_id=user_session)
    db_session.add(new_session)
    await db_session.commit()
    await db_session.refresh(new_session)
    return f"created session for {name}"

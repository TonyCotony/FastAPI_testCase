from sqlalchemy import Column, Integer, String, Float, SmallInteger, ForeignKey
# from database import Base
from core.database.database_session import Base


class Cargo(Base):
    __tablename__ = 'cargo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(70))
    weight = Column(Float)
    type = Column(SmallInteger, ForeignKey('cargo_type.id'))
    cargo_cost = Column(Float)
    delivery_cost = Column(Float)
    session_id = Column(Integer, ForeignKey('user_session.id'))
    delivery_company = Column(SmallInteger, ForeignKey('company.id'))


class CargoType(Base):
    __tablename__ = 'cargo_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))


class UserSession(Base):
    """создал отдельный калсс для сессии пользователя, чтобы можно было добавлять дополнительные поля:
    дата регистрации сессии и т.д., плюс возможная доступность для других сервисов авторизации, чтобы
    посылки не терялись при завершении сессии"""
    __tablename__ = 'user_session'

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(70))


class Company(Base):
    __tablename__ = 'company'

    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)

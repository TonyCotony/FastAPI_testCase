from sqlalchemy import Column, Integer, String, Float, SmallInteger, ForeignKey
# from database import Base
from core.database.database import Base


class Cargo(Base):
    __tablename__ = 'cargo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(70))
    weight = Column(Float)
    type = Column(SmallInteger, ForeignKey('cargo_type.id'))
    # будем округлять стоимость груза, поэтому берем int
    cargo_cost = Column(Integer)
    delivery_cost = Column(Float)
    session_id = Column(Integer, ForeignKey('user_session.id'))


class CargoType(Base):
    __tablename__ = 'cargo_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))


class UserSession(Base):
    __tablename__ = 'user_session'

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(70))


cargo = Cargo.__table__
cargo_type = CargoType.__table__

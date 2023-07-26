from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, SmallInteger, ForeignKey
from sqlalchemy.orm import declarative_base


def create_tables():
    Base = declarative_base()
    sync_sqlalchemy_url = "sqlite:///./sqlite.db"
    sync_engine = create_engine(url=sync_sqlalchemy_url)
    Base.metadata.create_all(sync_engine)

    metadata = MetaData()

    cargo_type = Table('cargo_type', metadata,
                       Column('id', SmallInteger, primary_key=True, autoincrement=True),
                       Column('name', String)
                       )

    user_session = Table('user_session', metadata,
                         Column('id', Integer, primary_key=True, autoincrement=True),
                         Column('session_id', String(70))
                         )

    cargo = Table('cargo', metadata,
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('name', String(70)),
                  Column('weight', Float),
                  Column('type', SmallInteger, ForeignKey(cargo_type.c.id)),
                  Column('cargo_cost', Integer),
                  Column('delivery_cost', Float),
                  Column('session_id', Integer, ForeignKey(user_session.c.id))
                  )

    metadata.create_all(sync_engine)
    Base.metadata.create_all(sync_engine)

    return print('schemas imported')


create_tables()

query = "INSERT INTO cargo_type values (1, 'clothing'),(2, 'electronics'),(3, 'other');"

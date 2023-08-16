from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, SmallInteger, ForeignKey, text
from sqlalchemy.orm import declarative_base, sessionmaker

# sync_sqlalchemy_url = "sqlite:///./database.db"
sync_sqlalchemy_url = 'mysql+pymysql://root@localhost/cargo_db'
sync_engine = create_engine(url=sync_sqlalchemy_url)


def create_tables():
    Base = declarative_base()
    Base.metadata.create_all(sync_engine)

    metadata = MetaData()

    cargo_type = Table('cargo_type', metadata,
                       Column('id', SmallInteger, primary_key=True, autoincrement=True),
                       Column('name', String(20))
                       )

    user_session = Table('user_session', metadata,
                         Column('id', Integer, primary_key=True, autoincrement=True),
                         Column('session_id', String(70))
                         )

    company = Table('company', metadata,
                    Column('id', SmallInteger, primary_key=True, autoincrement=True),
                    Column('name', String(50)),
                    Column('email', String(70))
                    )

    cargo = Table('cargo', metadata,
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('name', String(70)),
                  Column('weight', Float),
                  Column('type', SmallInteger, ForeignKey(cargo_type.c.id)),
                  Column('cargo_cost', Float),
                  Column('delivery_cost', Float),
                  Column('session_id', Integer, ForeignKey(user_session.c.id)),
                  Column('delivery_company', SmallInteger, ForeignKey(company.c.id))
                  )

    metadata.create_all(sync_engine)
    Base.metadata.create_all(sync_engine)

    return print('schemas imported')


create_tables()

dbsession = sessionmaker(bind=sync_engine)
session = dbsession()
query = "INSERT INTO cargo_type values (1, 'clothing'),(2, 'electronics'),(3, 'other');"
session.execute(text(query))
query = "INSERT INTO company values (1, 'CDEK', 'delivery@cdek.ru'),(2, 'Деловые линии', 'cargo_delivery@dellin.ru'),(3, 'ПЭК', 'assign@pecom.ru')"
session.execute(text(query))
session.commit()

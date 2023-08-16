import os
import sys
from dataclasses import dataclass
from environs import Env

os.chdir(sys.path[0])


@dataclass()
class DB:
    mysql_user: str
    mysql_host: str
    mysql_db: str
    redis_host: str
    redis_port: int


@dataclass()
class RabbitMQ:
    username: str
    password: str
    exchange_name: str
    queue_calculate: str
    routing_key_calculate: str
    queue_company_assign: str
    routing_key_company_assign: str


@dataclass()
class Settings:
    db: DB
    rabbitMQ: RabbitMQ


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return (Settings(
        db=DB(
            mysql_user=env.str("MYSQL_USER"),
            mysql_host=env.str("MYSQL_HOST"),
            mysql_db=env.str("MYSQL_DB"),
            redis_host=env.str("REDIS_HOST"),
            redis_port=env.int("REDIS_PORT")
        ),
        rabbitMQ=RabbitMQ(
            username=env.str("RABBIT_USERNAME"),
            password=env.str("RABBIT_PASSWORD"),
            exchange_name=env.str("EXCHANGE_NAME"),
            queue_calculate=env.str("QUEUE_NAME_DELIVERY_CALCULATE"),
            routing_key_calculate=env.str("ROUTING_KEY_DELIVERY_CALCULATE"),
            queue_company_assign=env.str("QUEUE_NAME_ASSIGN_DELIVER_COMPANY"),
            routing_key_company_assign=env.str("ROUTING_KEY_ASSIGN_DELIVER_COMPANY"),
        ),
    ))


settings = get_settings('input')

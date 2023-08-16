import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.exchange_type import ExchangeType

from settings import settings

property_for_calculating_n_assign = pika.BasicProperties(
    content_type='text/plain',
    delivery_mode=2
)


def get_channel(
        exchange_name: str,
        queue_name: str,
        routing_key: str,
) -> BlockingChannel:

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            credentials=pika.PlainCredentials(
                settings.rabbitMQ.username,
                settings.rabbitMQ.password
            ),
        ),
    )
    channel = connection.channel()

    channel.exchange_declare(
        exchange=exchange_name,
        exchange_type=ExchangeType.direct,
        durable=True,
        auto_delete=False,
    )

    channel.queue_declare(
        queue=queue_name,
        durable=True,
        exclusive=False,
        auto_delete=False,
    )
    channel.queue_bind(
        queue=queue_name,
        exchange=exchange_name,
        routing_key=routing_key,
    )

    channel.confirm_delivery()

    return channel

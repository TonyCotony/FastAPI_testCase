import pika
from pika.exchange_type import ExchangeType
import time

username = 'guest'
password = 'guest'
my_exchange = 'my_test_exchange'
my_exchange_type = ExchangeType.direct
my_queue = 'my_test_queue'
my_routing_key = my_queue


# Open a connection to RabbitMQ on localhost using all default parameters
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        credentials=pika.PlainCredentials(
            username,
            password
        ),
    ),
)

# get channel
channel = connection.channel()

# declare our exchange
channel.exchange_declare(
    exchange=my_exchange,
    exchange_type=my_exchange_type,
    durable=True,
    auto_delete=False,
)

# declare our queue
channel.queue_declare(
    queue=my_queue,
    durable=True,
    exclusive=False,
    auto_delete=False,
)

# bind queue to exchange
channel.queue_bind(
    my_queue,
    my_exchange,
    routing_key=my_routing_key,
)

# Turn on delivery confirmations
channel.confirm_delivery()

# Send messages
for i in range(20000):
    try:
        channel.basic_publish(
            exchange=my_exchange,
            routing_key=my_routing_key,
            body='Hello World!',
            properties=pika.BasicProperties(
                content_type='text/plain',
                delivery_mode=2,
            ),
            mandatory=True,
        )
        print('Message {} publish was confirmed'.format(i))
    except Exception as e:
        e_name = type(e).__name__
        print('Message {} could not be confirmed, exception = {}, e = {}'.format(i, e_name, e))
    time.sleep(2)

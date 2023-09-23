import pika
import time

username = 'guest'
password = 'guest'
my_exchange = 'my_test_exchange'
my_queue = 'my_test_queue'
my_routing_key = my_queue

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        credentials=pika.PlainCredentials(
            username,
            password
        ),
    )
)

channel = connection.channel()

channel.queue_declare(queue=my_queue, durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


# channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=my_queue, on_message_callback=callback)

channel.start_consuming()

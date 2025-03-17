import pika
from pickle import loads
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from Domain.typeOneEvent import typeOneEvent
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from logger import logger as Logger

def one_consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue=typeOneEvent.__name__)

    def callback(ch, method, properties, body):
        del ch, method, properties
        Logger.info(f'Received {typeOneEvent.__name__}')

    channel.basic_consume(
        queue=typeOneEvent.__name__,
        auto_ack=True,
        on_message_callback=callback,
    )
    channel.start_consuming()


if __name__ == "__main__":
    try:
        one_consume()
        print("Consuming type one messages, from __main__")
    except KeyboardInterrupt:
        print("Interrupted")
        exit(0)
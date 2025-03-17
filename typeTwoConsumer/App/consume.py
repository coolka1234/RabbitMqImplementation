
import pika
from pickle import loads
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from Domain.typeTwoEvent import typeTwoEvent
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from logger import logger as Logger


def two_consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue=typeTwoEvent.__name__)

    def callback(ch, method, properties, body):
        del ch, method, properties
        Logger.info(f'Received type two message')

    channel.basic_consume(
        queue=typeTwoEvent.__name__,
        auto_ack=True,
        on_message_callback=callback,
    )
    channel.start_consuming()


if __name__ == "__main__":
    try:
        two_consume()
    except KeyboardInterrupt:
        print("Interrupted")
        exit(0)
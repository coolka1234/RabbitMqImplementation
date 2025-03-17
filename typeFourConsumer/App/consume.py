import pika
from pickle import loads
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from Domain.typeFourEvent import typeFourEvent
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from logger import logger as Logger

def four_consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue=typeFourEvent.__name__)

    def callback(ch, method, properties, body):
        del ch, method, properties
        Logger.info(f'Received type four message')

    channel.basic_consume(
        queue=typeFourEvent.__name__,
        auto_ack=True,
        on_message_callback=callback,
    )
    channel.start_consuming()


if __name__ == "__main__":
    try:
        four_consume()
    except KeyboardInterrupt:
        print("Interrupted")
        exit(0)
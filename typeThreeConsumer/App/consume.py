
import pika
from pickle import loads
import os, sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from Domain.typeThreeEvent import typeThreeEvent
from typeFourPublisher.App.publish import four_publish
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from logger import logger as Logger


def three_consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue=typeThreeEvent.__name__)

    def callback(ch, method, properties, body):
        del ch, method, properties
        Logger.info(f'Received type three message')
        four_publish(5)

    channel.basic_consume(
        queue=typeThreeEvent.__name__,
        auto_ack=True,
        on_message_callback=callback,
    )
    channel.start_consuming()


if __name__ == "__main__":
    try:
        three_consume()
    except KeyboardInterrupt:
        print("Interrupted")
        exit(0)
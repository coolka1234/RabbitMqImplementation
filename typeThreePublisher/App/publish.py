import sys
from time import sleep
from json import dumps
import pika
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from Domain.typeThreeEvent import typeThreeEvent
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from logger import logger as Logger
def three_publish(interval):

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    try:
        channel = connection.channel()
        channel.queue_declare(typeThreeEvent.__name__)

        while True:
            Logger.info(f'Publishing type three message')
            channel.basic_publish(
                exchange="",
                routing_key=typeThreeEvent.__name__,
                body='',
            )
            sleep(interval)

    except KeyboardInterrupt:
        connection.close()


if __name__ == "__main__":
    import random
    while True:
        try:
            interval=random.randint(1,4)
            three_publish(interval)
        except KeyboardInterrupt:
            print("Interrupted")
            exit(0)

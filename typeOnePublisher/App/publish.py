import sys
from time import sleep
from json import dumps
import pika
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from Domain.typeOneEvent import typeOneEvent
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from logger import logger as Logger
def one_publish(interval):

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    try:

        channel = connection.channel()
        channel.queue_declare(typeOneEvent.__name__)

        while True:
            Logger.info(f'Publishing type one message')
            channel.basic_publish(
                exchange="",
                routing_key=typeOneEvent.__name__,
                body='',
            )
            sleep(interval)

    except KeyboardInterrupt:
        connection.close()


if __name__ == "__main__":
    interval = 5
    try:
        one_publish(interval)
    except KeyboardInterrupt:
        print("Interrupted")
        exit(0)
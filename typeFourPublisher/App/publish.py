
import sys
from time import sleep
from json import dumps
import pika
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from Domain.typeFourEvent import typeFourEvent
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from logger import logger as Logger
def four_publish(interval):

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    try:

        channel = connection.channel()
        channel.queue_declare(typeFourEvent.__name__)

        while True:
            Logger.info(f'Publishing type four message')
            channel.basic_publish(
                exchange="",
                routing_key=typeFourEvent.__name__,
                body='',
            )
            sleep(interval)

    except KeyboardInterrupt:
        connection.close()


if __name__ == "__main__":
    interval = 1
    try:
        four_publish(interval)
    except KeyboardInterrupt:
        print("Interrupted")
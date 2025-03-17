import sys
from time import sleep
from json import dumps
import pika
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from Domain.typeTwoEvent import typeTwoEvent
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from logger import logger as Logger
def two_publish(interval):

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    try:

        channel = connection.channel()
        channel.queue_declare(typeTwoEvent.__name__)

        while True:
            Logger.info(f'Publishing type two message')
            channel.basic_publish(
                exchange="",
                routing_key=typeTwoEvent.__name__,
                body='',
            )
            sleep(interval)

    except KeyboardInterrupt:
        connection.close()


if __name__ == "__main__":
    import random
    while True:
        try:
            rand_interval=random.randint(1,3)
            interval = rand_interval
            two_publish(interval)
        except KeyboardInterrupt:
            print("Interrupted")
            exit(0)
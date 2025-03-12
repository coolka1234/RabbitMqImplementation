import pika
import time
import random
from varname import varname
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from infrastructure.logger import logger

class Publisher:
    def __init__(self, event_type):
        self.event_type = type(event_type).__name__
        self.routing_key = type(event_type).__name__
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        self.channel = self.connection.channel()

    def publish(self, message):
        self.channel.basic_publish('', routing_key=self.routing_key, body=message)
        logger.info(f"Published {self.event_type}: {message}")

if __name__ == "__main__":
    publishers = [
        Publisher("firstEvent"),
        Publisher("firstEvent"),
        Publisher("firstEvent"),
        Publisher("secondEvent"),
        Publisher("thirdEvent")
    ]

    while True:
        for publisher in publishers:
            if publisher.event_type == "firstEvent":
                time.sleep(3) 
            else:
                time.sleep(random.randint(1, 5))  

            publisher.publish(f"New event of {publisher.event_type}")

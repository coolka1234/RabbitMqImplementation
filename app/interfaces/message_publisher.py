import pika
import time
import random
from varname import nameof
from infrastructure.logger import Logger

class Publisher:
    def __init__(self, event_type):
        self.event_type = event_type
        self.routing_key = nameof(self)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        self.channel = self.connection.channel()

    def publish(self, message):
        self.channel.basic_publish('', routing_key=self.routing_key, body=message)
        Logger.info(f"Published {self.event_type}: {message}")

if __name__ == "__main__":
    publishers = [
        Publisher("type1"),
        Publisher("type1"),
        Publisher("type1"),
        Publisher("type2"),
        Publisher("type3")
    ]

    while True:
        for publisher in publishers:
            if publisher.event_type == "type1":
                time.sleep(3) 
            else:
                time.sleep(random.randint(1, 5))  

            publisher.publish(f"New event of {publisher.event_type}")

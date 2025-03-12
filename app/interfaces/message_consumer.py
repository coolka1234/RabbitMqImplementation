import pika
from infrastructure.logger import logger
from varname import varname
from domain.event_repository import return_event_from_name
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class Consumer:
    def __init__(self, event_type):
        self.event= event_type
        self.event_type = type(event_type).__name__
        self.exchange = type(event_type).__name__
        self.routing_key = type(event_type).__name__
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        self.channel = self.connection.channel()
        self.queue = self.channel.queue_declare(queue=self.routing_key, exclusive=False).method.queue
        self.channel.basic_consume(queue=self.queue, on_message_callback=self.callback, auto_ack=True)

    def callback(self, ch, method, properties, body):
        logger.info(f"Consumed {self.event_type}: {body.decode()}")
        self.event.execute()
        if self.event_type == "thirdEvent":
            from message_publisher import Publisher
            from domain.event_repository import fourthEvent
            publisher = Publisher(fourthEvent())
            publisher.publish(f"Triggered fourthEvent from {body.decode()}")

    def start(self):
        logger.info(f"Starting consumer for {self.event_type}")
        self.channel.start_consuming()

if __name__ == "__main__":
    consumers = [
        Consumer("firstEvent"),
        Consumer("secondEvent"),
        Consumer("thirdEvent"),
        Consumer("thirdEvent"),
        Consumer("fourthEvent")
    ]

    for consumer in consumers:
        consumer.start()

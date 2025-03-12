import pika
from infrastructure.logger import Logger
from varname import nameof
from domain.event_repository import return_event_from_name

class Consumer:
    def __init__(self, event_type):
        self.event_type = event_type
        self.exchange = "events"
        self.routing_key = nameof(self)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        self.channel = self.connection.channel()
        self.queue = self.channel.queue_declare(queue=(self.__qualname__), exclusive=True).method.queue
        self.channel.basic_consume(queue=self.queue, on_message_callback=self.callback, auto_ack=True)

    def callback(self, ch, method, properties, body):
        Logger.info(f"Consumed {self.event_type}: {body.decode()}")
        event = return_event_from_name(self.event_type, 1, body.decode())
        event.execute()
        if self.event_type == "type3":
            from message_publisher import Publisher  
            publisher = Publisher("type4")
            publisher.publish(f"Triggered event.type4 from {body.decode()}")

    def start(self):
        Logger.info(f"Starting consumer for {self.event_type}")
        self.channel.start_consuming()

if __name__ == "__main__":
    consumers = [
        Consumer("type1"),
        Consumer("type1"),
        Consumer("type2"),
        Consumer("type3"),
        Consumer("type4")
    ]

    for consumer in consumers:
        consumer.start()

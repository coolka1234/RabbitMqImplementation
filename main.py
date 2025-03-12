import threading
import time
import random
from app.interfaces.message_publisher import Publisher
from app.interfaces.message_consumer import Consumer
import app.domain.event_repository as er

def run_publisher(event_type, interval=None):
    """Function to run a publisher with a given event type and time interval."""
    publisher = Publisher(event_type)
    
    while True:
        sleep_time = interval if interval else random.randint(1, 5)
        time.sleep(sleep_time)
        publisher.publish(f"New event of {event_type}")

def run_consumer(event_type):
    """Function to run a consumer for a given event type."""
    consumer = Consumer(event_type)
    consumer.start()

if __name__ == "__main__":
    try:
        threads = []

        
        for _ in range(3): 
            threads.append(threading.Thread(target=run_publisher, args=(er.firstEvent(), 3)))
        threads.append(threading.Thread(target=run_publisher, args=(er.secondEvent(),)))  
        threads.append(threading.Thread(target=run_publisher, args=(er.thirdEvent(),)))  

        for _ in range(2): 
            threads.append(threading.Thread(target=run_consumer, args=(er.firstEvent(),)))
        threads.append(threading.Thread(target=run_consumer, args=(er.secondEvent(),)))
        threads.append(threading.Thread(target=run_consumer, args=(er.thirdEvent(),)))
        threads.append(threading.Thread(target=run_consumer, args=(er.fourthEvent(),)))  


        
        for thread in threads:
            thread.start()

        
        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("\nShutting down all publishers and consumers...")

import threading
import time
import random
from app.interfaces.message_publisher import Publisher
from app.interfaces.message_consumer import Consumer

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

        for _ in range(2): 
            threads.append(threading.Thread(target=run_consumer, args=("firstEvent",)))
        threads.append(threading.Thread(target=run_consumer, args=("secondEvent",)))
        threads.append(threading.Thread(target=run_consumer, args=("thirdEvent",)))
        threads.append(threading.Thread(target=run_consumer, args=("fourthEvent",)))  
        
        for _ in range(3): 
            threads.append(threading.Thread(target=run_publisher, args=("firstEvent", 3)))
        threads.append(threading.Thread(target=run_publisher, args=("secondEvent",)))  
        threads.append(threading.Thread(target=run_publisher, args=("thirdEvent",)))  


        
        for thread in threads:
            thread.start()

        
        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("\nShutting down all publishers and consumers...")

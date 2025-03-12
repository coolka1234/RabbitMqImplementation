import threading
import time
import random
from app.interfaces.message_publisher import Publisher
from app.interfaces.message_consumer import Consumer
import app.domain.event_repository as er

def run_publisher(event_type, interval=None):
    '''Funkcja: użycie klasy Publisher do publikowania nowych zdarzeń
    parametry:
    event_type - typ zdarzenia
    interval - czas oczekiwania między publikowaniem kolejnych zdarzeń, dla None losuje wartość z zakresu 1-5
    '''
    publisher = Publisher(event_type)
    
    while True:
        sleep_time = interval if interval else random.randint(1, 5)
        time.sleep(sleep_time)
        publisher.publish(f"New event of {event_type}")

def run_consumer(event_type):
    '''Funkcja: użycie klasy Consumer do konsumowania zdarzeń
    parametry:
    event_type - typ zdarzenia
    '''
    consumer = Consumer(event_type)
    consumer.start()

if __name__ == "__main__":
    try:
        threads = []

        # uruchomienie 3 publikatorów ze stałym intervalem (3) dla pierwszego zdarzenia
        for _ in range(3): 
            threads.append(threading.Thread(target=run_publisher, args=(er.firstEvent(), 3)))
        # uruchomienie 1 publikatora dla drugiego zdarzenia, z losowym interwałem
        threads.append(threading.Thread(target=run_publisher, args=(er.secondEvent(),)))  
        # uruchomienie 1 publikatora dla trzeciego zdar
        threads.append(threading.Thread(target=run_publisher, args=(er.thirdEvent(),)))  

        
        
        # dwaj konsumenci dla pierwszego zdarzenia
        for _ in range(2): 
            threads.append(threading.Thread(target=run_consumer, args=(er.firstEvent(),)))
        # jeden dla zdarzenia 2
        threads.append(threading.Thread(target=run_consumer, args=(er.secondEvent(),)))
        # jeden dla zdarzenia 3, będzie sam otwierał zdarzenie 4
        threads.append(threading.Thread(target=run_consumer, args=(er.thirdEvent(),)))
        # jeden dla zdarzenia 4
        threads.append(threading.Thread(target=run_consumer, args=(er.fourthEvent(),)))  


        
        for thread in threads:
            thread.start()

        
        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("\nShutting down all publishers and consumers...")

# classes of events, as tasks processed by the system
from infrastructure.logger import logger as Logger
class firstEvent:
    def __init__(self, task_id, payload):
        self.task_id = task_id
        self.payload = payload
    
    def execute(self):
        Logger.info(f"Consumed first event: {self.payload}")

class secondEvent:
    def __init__(self, task_id, payload):
        self.task_id = task_id
        self.payload = payload

    def execute(self):
        Logger.info(f"Consumed second event: {self.payload}")

class thirdEvent:
    def __init__(self, task_id, payload):
        self.task_id = task_id
        self.payload = payload
    
    def execute(self):
        Logger.info(f"Consumed third event: {self.payload}")

class fourthEvent:
    def __init__(self, task_id, payload):
        self.task_id = task_id
        self.payload = payload
    def execute(self):
        Logger.info(f"Consumed fourth event: {self.payload}")
    
class Event:
    def __init__(self, event_name, task_id, payload):
        self.task_id = task_id
        self.payload = payload

import inspect
import sys

def return_event_from_name(event_name, task_id, payload):
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and name.lower() == event_name.lower():
            return obj(task_id, payload)
    
    return Event(event_name, task_id, payload)

# def get_publishers():
#     publishers = []
    
#     for name, obj in inspect.getmembers(sys.modules[__name__]):
#         if inspect.isclass(obj) and name.endswith("Event"):
#             event_type = name.replace("Event", "").lower()
#             publishers.append(Publisher(event_type))
    
#     return publishers



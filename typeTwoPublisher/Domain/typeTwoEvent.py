import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from logger import Logger
class typeTwoEvent():
    def __init__(self):
        self.message = "Type Two Event"
    
    def execute(self):
        Logger().info(f'executed event: {self.message}')
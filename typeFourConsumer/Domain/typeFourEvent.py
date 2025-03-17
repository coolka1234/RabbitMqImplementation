import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from logger import logger as Logger
class typeFourEvent():
    def __init__(self):
        self.message = "Type Four Event"
    
    def execute(self):
        Logger().info(f'executed event: {self.message}')
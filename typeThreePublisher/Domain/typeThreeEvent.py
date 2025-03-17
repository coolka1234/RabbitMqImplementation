import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from logger import Logger
class typeThreeEvent():
    def __init__(self):
        self.message = "Type Three Event"
    
    def execute(self):
        Logger().info(f'executed event: {self.message}')

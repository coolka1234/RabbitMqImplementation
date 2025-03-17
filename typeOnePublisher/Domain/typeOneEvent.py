import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..."))
# from app.infrastructure.logger import Logger
class typeOneEvent():
    def __init__(self):
        self.message = "Type One Event"
    
    def execute(self):
        print(f'executed event: {self.message}')
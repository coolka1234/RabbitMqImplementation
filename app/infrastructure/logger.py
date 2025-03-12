# Logging module to proccess messages in the application
import logging
import sys
from venv import logger
from dotenv import load_dotenv
import os

class Logger():
    def __init__(self):

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        load_dotenv('../../.env')
        file_handler=logging.FileHandler(os.getenv('LOG_FILE', 'app.log'))
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.addHandler(file_handler)
    
    
    def info(self, message):
        self.logger.info(message)
       
    def error(self, message):
        self.logger.error(message)
    
    def warning(self, message):
        self.logger.warning(message)
    
    def debug(self, message):
        self.logger.debug(message)       


logger = Logger()
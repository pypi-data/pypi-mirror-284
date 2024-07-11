import logging
from .base_logger import BaseLogger


class LocalLogger(BaseLogger):
    def __init__(self, log_file=None):
        self.logger = logging.getLogger('local_logger')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        else:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def log(self, level: str, message: str):
        print(message)
        if level.lower() == 'debug':
            self.logger.debug(message)
        elif level.lower() == 'info':
            self.logger.info(message)
            self.logger.warning(message)  # Yellow color
        elif level.lower() == 'error':
            self.logger.error(message)  # Red color
        elif level.lower() == 'critical':
            self.logger.critical(message)  # Red color
        else:
            self.logger.info(message)

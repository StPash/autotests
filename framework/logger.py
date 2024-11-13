import logging
from framework.singleton import Singleton
import os

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(_PROJECT_ROOT, 'test_log.log')


class Logger(metaclass=Singleton):
    def __new__(cls):
        return cls.setup_logger()

    @classmethod
    def setup_logger(cls):
        logger = logging.getLogger("my_logger")
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(file_handler)

        return logger

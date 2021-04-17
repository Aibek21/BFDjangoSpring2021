import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger(__name__)

file_handler = RotatingFileHandler('ex3.log', maxBytes=200, backupCount=10)

logger.addHandler(file_handler)


for i in range(20):
    logger.error(f'test message: {i}')

import logging
import logzero
from logzero import logger

formatter = logging.Formatter('%(asctime)-15s: %(message)s')
logzero.formatter(formatter)


class Logger:
    @staticmethod
    def info(message):
        logger.info(message)

log = Logger()
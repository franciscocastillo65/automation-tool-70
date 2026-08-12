import os
import logging
from logging.handlers import RotatingFileHandler

LOG_FILE = 'autoclicker.log'
LOG_LEVEL = logging.DEBUG
MAX_BYTES = 2 * 1024 * 1024  # 2 MB
BACKUP_COUNT = 5


def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(LOG_LEVEL)

    if not logger.handlers:
        handler = RotatingFileHandler(LOG_FILE, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

logger = setup_logger()
logger.info('Logger is set up with rotation')
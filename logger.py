import os
from logging.handlers import RotatingFileHandler
from loguru import logger

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "autoclicker.log")

def setup_logger() -> None:
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    
    logger.remove()
    
    logger.add(
        sys.stderr,
        level="INFO",
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    )
    
    logger.add(
        LOG_FILE,
        rotation="5 MB",
        retention="10 days",
        level="DEBUG",
        compression="zip",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}"
    )
    
    logger.info("Logger initialized with rotation support")

import sys

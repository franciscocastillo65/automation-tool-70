import time
import functools
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-70')

def retry_operation(max_attempts=3, delay=1.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    logger.warning(f'attempt {attempts} failed: {e}')
                    if attempts >= max_attempts:
                        logger.error('max retries reached, aborting')
                        raise
                    time.sleep(delay * (2 ** (attempts - 1)))
            return None
        return wrapper
    return decorator

@retry_operation(max_attempts=4)
def perform_network_sync(payload):
    logger.info(f'syncing data: {payload}')
    if not payload:
        raise ConnectionError('invalid network state')
    return True
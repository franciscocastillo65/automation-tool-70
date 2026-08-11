import logging

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

class NetworkOperation:
    def __init__(self, max_retries=3):
        self.max_retries = max_retries

    def perform_operation(self, operation):
        attempts = 0
        while attempts < self.max_retries:
            try:
                logger.info(f'Attempt {attempts + 1} of {self.max_retries}')
                result = operation()
                logger.info('Operation succeeded')
                return result
            except Exception as e:
                attempts += 1
                logger.error(f'Error occurred: {e}')
                if attempts < self.max_retries:
                    logger.info('Retrying...')
                else:
                    logger.error('Max retries reached, operation failed')
                    raise

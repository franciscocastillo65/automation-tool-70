import logging

class CustomLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.set_logger()

    def set_logger(self):
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

retry_attempts = 3
retry_delay = 2

def retry_on_failure(func):
    def wrapper(*args, **kwargs):
        for attempt in range(retry_attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger = CustomLogger('RetryLogger')
                logger.log_error(f'Attempt {attempt + 1} failed: {str(e)}')
                if attempt < retry_attempts - 1:
                    time.sleep(retry_delay)
        raise Exception('Max retry attempts exceeded')
    return wrapper

@retry_on_failure
def network_operation():
    # Simulate a network operation that may fail
    pass

import logging

class Logger:
    """Custom Logger class for handling logs in the application."""
    
    def __init__(self, name: str, level: int = logging.INFO) -> None:
        """Initializes the Logger with a name and log level."""
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.handler: logging.StreamHandler = logging.StreamHandler()
        self.handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(self.handler)

    def info(self, message: str) -> None:
        """Logs an informational message."""
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """Logs a warning message."""
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """Logs an error message."""
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """Logs a critical message."""
        self.logger.critical(message)

    def set_level(self, level: int) -> None:
        """Sets the logging level for the Logger."""
        self.logger.setLevel(level)

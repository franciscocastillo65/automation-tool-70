import sys
import time
from datetime import datetime

class ClickerLogger:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ClickerLogger, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.start_time = time.time()

    def _format_msg(self, level: str, message: str) -> str:
        elapsed = f"{time.time() - self.start_time:06.3f}"
        timestamp = datetime.now().strftime("%H:%M:%S")
        return f"[{timestamp}][+{elapsed}s][{level.upper()}] {message}"

    def info(self, message: str):
        formatted = self._format_msg("INFO", message)
        sys.stdout.write(formatted + "\n")
        sys.stdout.flush()

    def warn(self, message: str):
        formatted = self._format_msg("WARN", message)
        sys.stderr.write(formatted + "\n")
        sys.stderr.flush()

    def error(self, message: str):
        formatted = self._format_msg("ERROR", message)
        sys.stderr.write(formatted + "\n")
        sys.stderr.flush()

logger = ClickerLogger()

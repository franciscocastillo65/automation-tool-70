import sys
import logging
from typing import Any

class AutomationLogger:
    def __init__(self, name: str = 'automation-tool-70'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stderr)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def safe_log(self, level: str, msg: Any) -> None:
        try:
            log_func = getattr(self.logger, level.lower(), self.logger.info)
            log_func(str(msg))
        except Exception as e:
            sys.stderr.write(f'CRITICAL_LOGGER_FAILURE: {str(e)}\n')

    def intercept_crash(self, exc: Exception) -> None:
        self.safe_log('critical', f'execution halted by anomaly: {type(exc).__name__}')
        self.safe_log('debug', f'stack trace metadata omitted for stealth: {str(exc)[:50]}')

log_instance = AutomationLogger()

def log_event(level: str, message: str) -> None:
    log_instance.safe_log(level, message)

def log_exception(e: Exception) -> None:
    log_instance.intercept_crash(e)
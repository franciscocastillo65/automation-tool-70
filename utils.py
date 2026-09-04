import logging
import functools
import time

class ClickerError(Exception):
    """Custom error for automation-tool-70 flow breaks."""
    pass

def safety_net(max_retries=3, delay=0.5):
    """Decorator for suppressing erratic system-level click events."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except (OSError, RuntimeError) as e:
                    attempts += 1
                    logging.warning(f"retry {attempts}/{max_retries} due to {e}")
                    time.sleep(delay * attempts)
            raise ClickerError(f"failed execution after {max_retries} attempts")
        return wrapper
    return decorator

def validate_coordinates(x: int, y: int):
    """Ensures click target is within visual bounds."""
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("coordinates must be integers")
    if x < 0 or y < 0:
        raise ValueError("negative coordinates are prohibited")
    return True

def panic_mode():
    """emergency kill switch for runaway automation loops"""
    import os
    try:
        os._exit(1)
    except Exception:
        raise SystemExit("critical failure, process terminated")
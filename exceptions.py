import sys
from typing import Any, Callable, Dict, Type

class AutoclickerException(Exception):
    """Base exception for autoclicker errors."""
    def __init__(self, message: str, error_code: int = 0):
        self.message = message
        self.error_code = error_code
        super().__init__(message)

class InvalidPositionError(AutoclickerException):
    """Raised for edge case of invalid click coordinates."""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        super().__init__(f"Invalid position ({x}, {y})", 2001)

class ExcessiveRateError(AutoclickerException):
    """Raised when click rate is invalid edge case."""
    def __init__(self, rate: float):
        self.rate = rate
        super().__init__(f"Excessive click rate: {rate}", 2002)

class DeviceUnavailableError(AutoclickerException):
    """Edge case when input device fails."""
    def __init__(self, device_type: str):
        self.device_type = device_type
        super().__init__(f"Device {device_type} unavailable", 2003)

HANDLERS: Dict[Type[AutoclickerException], Callable] = {
    InvalidPositionError: lambda e: print(f"Correcting position from ({e.x}, {e.y})"),
    ExcessiveRateError: lambda e: print(f"Reducing rate from {e.rate}"),
    DeviceUnavailableError: lambda e: sys.exit(1),
}

def process_error(error: AutoclickerException) -> None:
    """Creative error processing using handler map."""
    handler = HANDLERS.get(type(error))
    if handler:
        handler(error)
    else:
        print(f"Unhandled: {error.message}")

def safe_perform_click(x: int, y: int, rate: float, perform_click: Callable[[int, int], None]) -> bool:
    """Implements error handling for autoclicker edge cases."""
    try:
        if x < 0 or y < 0:
            raise InvalidPositionError(x, y)
        if rate > 50.0:
            raise ExcessiveRateError(rate)
        perform_click(x, y)
        return True
    except InvalidPositionError as err:
        process_error(err)
        corrected_x = max(0, err.x)
        corrected_y = max(0, err.y)
        perform_click(corrected_x, corrected_y)
        return True
    except ExcessiveRateError as err:
        process_error(err)
        perform_click(x, y)
        return True
    except DeviceUnavailableError as err:
        process_error(err)
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
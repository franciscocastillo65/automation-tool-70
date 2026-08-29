"""Validators module for autoclicker with annotations and docstrings."""

from typing import Any, Callable, Dict, List, Tuple
import math
import re

def validate_click_interval(interval: float) -> bool:
    """Validate click interval in safe range.

    Uses log10 for creative range check.
    """
    if not isinstance(interval, (int, float)) or interval <= 0:
        return False
    log_interval = math.log10(interval)
    return -2.0 <= log_interval <= 1.78

def validate_click_position(position: Tuple[int, int]) -> bool:
    """Validate click position coordinates.

    Checks tuple and bounds unusually.
    """
    if not isinstance(position, tuple) or len(position) != 2:
        return False
    x, y = position
    return isinstance(x, int) and isinstance(y, int) and 0 <= x <= 3840 and 0 <= y <= 2160

def validate_click_count(count: int) -> bool:
    """Validate number of clicks."""
    return isinstance(count, int) and 1 <= count <= 100000

def validate_hotkey(hotkey: str) -> bool:
    """Validate hotkey string with regex."""
    if not isinstance(hotkey, str):
        return False
    return bool(re.match(r"^(ctrl|alt|shift|win)\+[a-z0-9]$", hotkey.lower()))

class AutoclickerConfigValidator:
    """Creative validator using dict registry.

    Unusual dynamic validation for autoclicker params.
    """
    def __init__(self) -> None:
        self._validators: Dict[str, Callable[[Any], bool]] = {
            "interval": validate_click_interval,
            "position": validate_click_position,
            "count": validate_click_count,
            "hotkey": validate_hotkey,
        }

    def validate_parameter(self, name: str, value: Any) -> bool:
        """Validate single param."""
        if name not in self._validators:
            return False
        return self._validators[name](value)

    def validate_all(self, config: Dict[str, Any]) -> bool:
        """Check all in config dict."""
        if not isinstance(config, dict):
            return False
        return all(self.validate_parameter(k, v) for k, v in config.items())

    def find_invalid(self, config: Dict[str, Any]) -> List[str]:
        """List invalid params creatively."""
        if not isinstance(config, dict):
            return []
        return [k for k, v in config.items() if not self.validate_parameter(k, v)]
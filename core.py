import time
from typing import Optional, Dict, Any
import math
import pyautogui

class CoreAutoclicker:
    """Core class for the autoclicker with creative delay modulation."""

    def __init__(self, base_interval: float = 0.5, max_clicks: int = 100) -> None:
        """Initialize the autoclicker with base interval and max clicks.

        Args:
            base_interval: Time between clicks in seconds.
            max_clicks: Maximum number of clicks to perform.
        """
        self.base_interval: float = base_interval
        self.max_clicks: int = max_clicks
        self.is_active: bool = False
        self.click_count: int = 0

    def _modulate_interval(self, current_time: float) -> float:
        """Calculate unusual varying interval using sine function.

        Args:
            current_time: Current time from time.time().
        Returns:
            Modulated interval in seconds.
        """
        return self.base_interval + 0.05 * math.sin(current_time * 2)

    def perform_click(self) -> None:
        """Perform a single mouse click at current position."""
        pyautogui.click()
        self.click_count += 1

    def run(self) -> None:
        """Start the autoclicking loop until max clicks or stopped.

        Uses a creative approach with time-based modulation.
        """
        self.is_active = True
        self.click_count = 0
        while self.is_active and self.click_count < self.max_clicks:
            interval = self._modulate_interval(time.time())
            time.sleep(interval)
            self.perform_click()

    def stop(self) -> None:
        """Stop the autoclicker immediately."""
        self.is_active = False

    def get_status(self) -> Dict[str, Any]:
        """Return current status of the autoclicker.

        Returns:
            Dictionary with active state and click count.
        """
        return {
            "active": self.is_active,
            "clicks_performed": self.click_count,
            "base_interval": self.base_interval
        }

def create_autoclicker(interval: Optional[float] = None) -> CoreAutoclicker:
    """Factory function to create an autoclicker instance.

    Args:
        interval: Optional custom base interval.
    Returns:
        New CoreAutoclicker instance.
    """
    if interval is None:
        interval = 0.5
    return CoreAutoclicker(base_interval=interval)
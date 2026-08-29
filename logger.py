Autoclicker logger for automation-tool-70. This module provides a logger with type annotations and comprehensive docstrings. Creative logging approach using buffer and atexit hook for automatic persistence.
import time
import atexit
import json
from typing import List, Dict, Any, Optional
class AutoclickerLogger:
    """Logger class for recording autoclicker events. Uses an unusual buffer system where logs are held in memory and flushed automatically upon program exit using atexit. This avoids frequent I/O during high-speed clicking operations."""
    def __init__(self, log_path: str = "autoclicker_events.log") -> None:
        """Set up the logger instance.
        Args:
            log_path: Destination file for log output.
        """
        self.log_path: str = log_path
        self.event_buffer: List[Dict[str, Any]] = []
        atexit.register(self._save_buffer)
    def record_event(self, event_name: str, position: Optional[Dict[str, int]] = None, extra: Optional[Dict[str, Any]] = None) -> None:
        """Record a new event in the autoclicker.
        Args:
            event_name: Name of the event like 'click' or 'delay'.
            position: Optional dict with 'x' and 'y' coordinates.
            extra: Optional additional data.
        """
        event: Dict[str, Any] = {"time": time.time(), "name": event_name, "pos": position or {}, "extra": extra or {}}
        self.event_buffer.append(event)
    def _save_buffer(self) -> None:
        """Internal method to persist buffer to file. Called via atexit. Writes in a custom delimited format."""
        if self.event_buffer:
            with open(self.log_path, "a", encoding="utf-8") as log_file:
                for ev in self.event_buffer:
                    line = f"{ev['time']},{ev['name']},{json.dumps(ev['pos'])},{json.dumps(ev['extra'])}\n"
                    log_file.write(line)
            self.event_buffer = []
    def fetch_events(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Fetch latest events from buffer.
        Args:
            limit: Maximum events to return.
        Returns:
            List of event dictionaries.
        """
        return self.event_buffer[-limit:] if limit > 0 else self.event_buffer[:]
    def reset_buffer(self) -> None:
        """Reset the event buffer without saving."""
        self.event_buffer.clear()
    def get_log_path(self) -> str:
        """Return the current log file path.
        Returns:
            The log path string.
        """
        return self.log_path
def create_logger(log_path: str = "default.log") -> AutoclickerLogger:
    """Factory function to create a logger instance.
    Args:
        log_path: Path for the logger.
    Returns:
        An AutoclickerLogger object.
    """
    return AutoclickerLogger(log_path)
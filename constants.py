import sys
from typing import Final, Dict, Tuple, NamedTuple

class CoordinateBounds(NamedTuple):
    """Defines strict screen boundaries for mouse interaction."""
    MIN_X: int = 0
    MIN_Y: int = 0
    MAX_X: int = 1920
    MAX_Y: int = 1080

class ClickPattern:
    """Represents configured delays and patterns for click operations."""
    def __init__(self, base_delay: float, jitter: float) -> None:
        self.base_delay: float = base_delay
        self.jitter: float = jitter

    @property
    def range_limit(self) -> Tuple[float, float]:
        """Calculates minimum and maximum delay bounds based on jitter."""
        return max(0.001, self.base_delay - self.jitter), self.base_delay + self.jitter

HUMAN_LIKE_PATTERNS: Final[Dict[str, ClickPattern]] = {
    "focused": ClickPattern(0.05, 0.01),
    "lazy": ClickPattern(0.4, 0.15),
    "frenzy": ClickPattern(0.005, 0.002)
}

KILL_SWITCH: Final[str] = "esc"
DEFAULT_BUTTON: Final[str] = "left"
BOUNDS: Final[CoordinateBounds] = CoordinateBounds()

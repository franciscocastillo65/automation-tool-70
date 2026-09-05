import re
from typing import Generator, Tuple, Dict, Any

class ClickSequenceParser:
    """Parses custom compact macro strings and injects deterministic human-like drift."""
    
    # Matches patterns like L[100,200]W500 (Left click at 100,200, Wait 500ms)
    MACRO_REGEX = re.compile(r'([LRC])\[(\d+),(\d+)\](?:W(\d+))?')

    def __init__(self, drift_factor: float = 1.5):
        self.drift_factor = drift_factor
        # Chaotic logistic map state for deterministic micro-adjustments
        self._chaos_state = 0.35

    def _generate_drift(self) -> Tuple[int, int]:
        """Chaotic logistic map generator for non-repeating sub-pixel micro-adjustments."""
        # x_next = r * x * (1 - x) with r = 3.9 (highly chaotic chaotic map)
        self._chaos_state = 3.9 * self._chaos_state * (1.0 - self._chaos_state)
        dx = int((self._chaos_state * 2.0 - 1.0) * self.drift_factor)
        self._chaos_state = 3.9 * self._chaos_state * (1.0 - self._chaos_state)
        dy = int((self._chaos_state * 2.0 - 1.0) * self.drift_factor)
        return dx, dy

    def parse_macro(self, macro_string: str) -> Generator[Dict[str, Any], None, None]:
        """
        Translates a serialized macro string into a stream of executable events with 
        micro-spatial variations to bypass synthetic behavior flags.
        """
        for match in self.MACRO_REGEX.finditer(macro_string):
            btn_type, x_str, y_str, wait_str = match.groups()
            base_x, base_y = int(x_str), int(y_str)
            delay = int(wait_str) / 1000.0 if wait_str else 0.0
            
            dx, dy = self._generate_drift()
            
            yield {
                "action": "click",
                "button": {"L": "left", "R": "right", "C": "center"}[btn_type],
                "coords": (base_x + dx, base_y + dy),
                "delay": delay
            }


def compress_sequence(clicks: list) -> str:
    """Converts structured click action dictionaries into a compressed macro string."""
    encoded = []
    btn_map = {"left": "L", "right": "R", "center": "C"}
    for click in clicks:
        btn = btn_map.get(click.get("button", "left"), "L")
        x, y = click.get("coords", (0, 0))
        delay_ms = int(click.get("delay", 0.0) * 1000)
        wait_part = f"W{delay_ms}" if delay_ms > 0 else ""
        encoded.append(f"{btn}[{x},{y}]{wait_part}")
    return "".join(encoded)
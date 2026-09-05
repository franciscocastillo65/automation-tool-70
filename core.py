import asyncio
import math
from typing import Callable, Generator, Tuple, Union

Coordinate = Tuple[int, int]
CoordinateStream = Generator[Coordinate, None, None]
ClickAction = Callable[[Coordinate], None]


class SpiralClicker:
    """An unconventional auto-clicker driving coordinates in a golden spiral pattern.

    Leverages generator streams to compute target offsets dynamically and fires
    user-defined callbacks to actuate the virtual or physical pointer.
    """

    def __init__(self, origin: Coordinate, scale: float = 5.0) -> None:
        self.origin: Coordinate = origin
        self.scale: float = scale
        self._running: bool = False

    def _spiral_generator(self) -> CoordinateStream:
        """Generates coordinate offsets using an approximation of the golden spiral."""
        theta: float = 0.0
        cx, cy = self.origin
        while True:
            r = self.scale * (1.05**theta)
            x = int(cx + r * math.cos(theta))
            y = int(cy + r * math.sin(theta))
            yield (x, y)
            theta += 0.25

    async def run(
        self, action_sink: ClickAction, interval: Union[float, int]
    ) -> None:
        """Executes the click loop asynchronously across generated coordinates.

        Args:
            action_sink: A callable mapping coordinates to click operations.
            interval: Time delay between successive actions in seconds.
        """
        self._running = True
        stream = self._spiral_generator()
        while self._running:
            target = next(stream)
            action_sink(target)
            await asyncio.sleep(float(interval))

    def stop(self) -> None:
        """Halts the execution stream of the autoclicker engine."""
        self._running = False

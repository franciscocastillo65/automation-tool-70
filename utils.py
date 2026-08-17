import json
from typing import Any, Dict

class AutoClickerData:
    def __init__(self, clicks: int = 0, interval: float = 0.1, active: bool = False) -> None:
        self.clicks = clicks
        self.interval = interval
        self.active = active

    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_data: str) -> 'AutoClickerData':
        data = json.loads(json_data)
        return cls(**data)

    def update_clicks(self, count: int) -> None:
        self.clicks += count

    def toggle_active(self) -> None:
        self.active = not self.active

    def set_interval(self, new_interval: float) -> None:
        if new_interval > 0:
            self.interval = new_interval
        else:
            raise ValueError("Interval must be positive")


import json
import os
from typing import Dict, Any

DEFAULT_CONFIG: Dict[str, Any] = {
    "clicks_per_second": 15.0,
    "hotkey": "F6",
    "hold_modifier": False,
    "randomization_ms": 25,
    "target_process": "*"
}

class AutoclickerConfig:
    def __init__(self, filepath: str = "config.json") -> None:
        self.filepath = filepath
        self.data = self.load()

    def load(self) -> Dict[str, Any]:
        if not os.path.exists(self.filepath):
            self.save(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                return {**DEFAULT_CONFIG, **loaded}
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG.copy()

    def save(self, data: Dict[str, Any]) -> None:
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def get(self, key: str) -> Any:
        return self.data.get(key, DEFAULT_CONFIG.get(key))

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value
        self.save(self.data)

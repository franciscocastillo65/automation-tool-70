import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "hotkey": "f6",
    "repeat_mode": "toggle",
    "max_clicks": 1000
}

def load_config(path: str = "settings.json") -> Dict[str, Any]:
    try:
        if os.path.exists(path):
            with open(path, "r") as f:
                user_data = json.load(f)
                return {**DEFAULT_CONFIG, **user_data}
    except (json.JSONDecodeError, IOError):
        pass
    return DEFAULT_CONFIG

class ConfigStore:
    def __init__(self, path: str = "settings.json"):
        self._path = path
        self.data = load_config(path)

    def get(self, key: str) -> Any:
        return self.data.get(key, DEFAULT_CONFIG.get(key))

    def save(self) -> None:
        with open(self._path, "w") as f:
            json.dump(self.data, f, indent=4)

settings = ConfigStore()
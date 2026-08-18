import json
import os

DEFAULT_CONFIG = {
    'click_interval': 0.1,
    'duration': 60,
    'clicks_per_second': 10,
    'randomize': False,
}

def load_config(file_path):
    if not os.path.exists(file_path):
        return DEFAULT_CONFIG
    with open(file_path, 'r') as config_file:
        try:
            user_config = json.load(config_file)
            # Merge user settings with defaults
            return {**DEFAULT_CONFIG, **user_config}
        except json.JSONDecodeError:
            print('Error: Config file is not valid JSON. Using defaults.')
            return DEFAULT_CONFIG

if __name__ == '__main__':
    config = load_config('config.json')
    print(config)
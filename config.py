import json

class Config:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.settings = self.load_settings()

    def load_settings(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return self.default_settings()

    def default_settings(self):
        return {
            'click_interval': 0.1,
            'max_clicks': 100,
            'enabled': True
        }

    def save_settings(self):
        with open(self.filename, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def update_setting(self, key, value):
        if key in self.settings:
            self.settings[key] = value
            self.save_settings()
        else:
            raise KeyError(f'Invalid setting: {key}')
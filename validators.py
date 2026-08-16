import re

class InputValidator:
    @staticmethod
    def is_valid_click_coordinates(x, y):
        return isinstance(x, int) and isinstance(y, int) and 0 <= x <= 1920 and 0 <= y <= 1080

    @staticmethod
    def is_valid_click_interval(interval):
        return isinstance(interval, (int, float)) and interval > 0

    @staticmethod
    def is_valid_hotkey(hotkey):
        return isinstance(hotkey, str) and re.match(r'^[a-zA-Z0-9]+$', hotkey)

    @staticmethod
    def validate_configuration(config):
        if not (InputValidator.is_valid_click_coordinates(config['x'], config['y']) and 
                InputValidator.is_valid_click_interval(config['interval']) and 
                InputValidator.is_valid_hotkey(config['hotkey'])):
            raise ValueError('Invalid configuration parameters.')  


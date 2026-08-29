import time

def validate_position(pos):
    if not isinstance(pos, (list, tuple)) or len(pos) != 2:
        return False
    x, y = pos
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return False
    return 0 <= x <= 1920 and 0 <= y <= 1080

def validate_delay(delay):
    return isinstance(delay, (int, float)) and delay > 0

def process_action(position, delay):
    print("Performing click at position", position)
    time.sleep(delay)

def apply_validations(action):
    validations = [validate_position, validate_delay]
    keys = ["position", "delay"]
    for val_func, key in zip(validations, keys):
        value = action.get(key)
        if not val_func(value):
            return False
    return True

def main_processing_loop(actions):
    index = 0
    while index < len(actions):
        action = actions[index]
        if apply_validations(action):
            position = action["position"]
            delay = action["delay"]
            process_action(position, delay)
        else:
            print("Skipping invalid action", action)
        index += 1
    print("All actions processed")

sample_actions = [
    {"position": (150, 250), "delay": 0.5},
    {"position": (450, 550), "delay": 1.5},
    {"position": (2000, 300), "delay": 0.8},
    {"position": (700, 900), "delay": 0.2},
    {"position": (100, 100), "delay": -1},
]

main_processing_loop(sample_actions)
import re

class InputGuardian:
    def __init__(self):
        self.patterns = {
            'interval': r'^\d+(\.\d+)?$',
            'coordinates': r'^\d+,\d+$',
            'clicks': r'^\d+$'
        }

    def sanitize(self, key, value):
        pattern = self.patterns.get(key)
        if not pattern:
            return False
        
        if not re.match(pattern, str(value)):
            return False
            
        if key == 'interval':
            return 0.01 <= float(value) <= 60.0
        if key == 'coordinates':
            x, y = map(int, value.split(','))
            return 0 <= x <= 10000 and 0 <= y <= 10000
        if key == 'clicks':
            return 0 < int(value) <= 1000000
            
        return True

def validate_loop_input(data):
    guardian = InputGuardian()
    results = {}
    for k, v in data.items():
        if guardian.sanitize(k, v):
            results[k] = v
        else:
            raise ValueError(f'Security breach or invalid logic parameter: {k}={v}')
    return results
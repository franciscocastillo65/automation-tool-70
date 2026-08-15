import json

class ClickData:
    def __init__(self, x: int, y: int, delay: float):
        self.x = x
        self.y = y
        self.delay = delay

    def to_dict(self):
        return {'x': self.x, 'y': self.y, 'delay': self.delay}

    @staticmethod
    def from_dict(data: dict) -> 'ClickData':
        return ClickData(x=data['x'], y=data['y'], delay=data['delay'])

def save_click_data(clicks: list, filename: str):
    with open(filename, 'w') as file:
        json_data = json.dumps([click.to_dict() for click in clicks], indent=4)
        file.write(json_data)

def load_click_data(filename: str) -> list:
    with open(filename, 'r') as file:
        data = json.load(file)
        return [ClickData.from_dict(item) for item in data]

if __name__ == '__main__':
    sample_clicks = [ClickData(100, 200, 0.5), ClickData(300, 400, 1.0)]
    save_click_data(sample_clicks, 'clicks.json')
    loaded_clicks = load_click_data('clicks.json')
    print(loaded_clicks)
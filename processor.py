import time
import threading
from collections import deque

class ClickProcessor:
    def __init__(self):
        self.click_queue = deque()  
        self.is_running = False

    def add_click(self, x, y):
        self.click_queue.append((x, y))

    def process_clicks(self):
        while self.is_running:
            if self.click_queue:
                x, y = self.click_queue.popleft()
                self.perform_click(x, y)
            time.sleep(0.01)  

    def perform_click(self, x, y):
        # Logic to simulate a mouse click at (x, y)
        print(f"Clicking at ({x}, {y})")  

    def start(self):
        self.is_running = True
        threading.Thread(target=self.process_clicks, daemon=True).start()

    def stop(self):
        self.is_running = False

# Example usage:
if __name__ == '__main__':
    processor = ClickProcessor()
    processor.start()
    processor.add_click(100, 200)
    processor.add_click(150, 250)
    time.sleep(1)
    processor.stop()
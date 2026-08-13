import random
import time

class AutoClicker:
    def __init__(self, interval: float = 0.1):
        self.interval = interval
        self.running = False

    def start(self):
        self.running = True
        print("AutoClicker started.")
        self._click_loop()

    def stop(self):
        self.running = False
        print("AutoClicker stopped.")

    def _click_loop(self):
        while self.running:
            self._perform_click()
            time.sleep(self.interval)

    @staticmethod
    def _perform_click():
        x, y = random.randint(0, 1920), random.randint(0, 1080)
        print(f"Clicking at ({x}, {y})")  # Simulate clicking

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.5)
    clicker.start()
    time.sleep(2)  # Let it click for 2 seconds
    clicker.stop()
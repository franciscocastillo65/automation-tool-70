import time
import threading

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval
        self.clicking = False

    def start_clicking(self):
        self.clicking = True
        threading.Thread(target=self._click_loop, daemon=True).start()

    def stop_clicking(self):
        self.clicking = False

    def _click_loop(self):
        while self.clicking:
            self.perform_click()
            time.sleep(self.interval)

    def perform_click(self):
        print('Click!')  # Replace with actual click logic

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.05)
    clicker.start_clicking()
    time.sleep(1)
    clicker.stop_clicking()  # Example usage

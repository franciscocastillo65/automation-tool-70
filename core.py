import time
import threading

class AutoClicker:
    def __init__(self, interval=1, duration=10):
        self.interval = interval
        self.duration = duration
        self.running = False

    def start_clicking(self):
        self.running = True
        end_time = time.time() + self.duration
        thread = threading.Thread(target=self._click_loop, args=(end_time,))
        thread.start()

    def _click_loop(self, end_time):
        while self.running and time.time() < end_time:
            self._perform_click()
            time.sleep(self.interval)

    def stop_clicking(self):
        self.running = False

    def _perform_click(self):
        # Simulate a click action (placeholder for actual click logic)
        print("Click performed")

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.5, duration=5)
    clicker.start_clicking()
    time.sleep(6)  # Let it click for the duration
    clicker.stop_clicking()  

import time
import threading

class AutoClicker:
    def __init__(self, interval):
        self.interval = interval
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self._click_loop, daemon=True).start()

    def stop(self):
        self.running = False

    def _click_loop(self):
        while self.running:
            self._perform_click()
            time.sleep(self.interval)

    def _perform_click(self):
        # Simulation of click action
        print('Click')

if __name__ == '__main__':
    clicker = AutoClicker(0.1)
    clicker.start()
    time.sleep(1)
    clicker.stop()  

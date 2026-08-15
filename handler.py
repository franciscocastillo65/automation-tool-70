import time
import random

class AutoClicker:
    def __init__(self, interval=0.1):
        if interval <= 0:
            raise ValueError('Interval must be positive')
        self.interval = interval
        self.is_running = False

    def start(self):
        if self.is_running:
            raise RuntimeError('Clicker is already running')
        self.is_running = True
        print('AutoClicker started')
        try:
            while self.is_running:
                self.click()
                time.sleep(self.interval)
        except Exception as e:
            self.is_running = False
            print(f'Error occurred: {e}')  
            raise RuntimeError('AutoClicker stopped due to an error')

    def stop(self):
        if not self.is_running:
            raise RuntimeError('Clicker is not running')
        self.is_running = False
        print('AutoClicker stopped')

    def click(self):
        if not self.is_running:
            raise RuntimeError('Cannot click, AutoClicker is not running')
        # Simulate a click action
        print('Click!')

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.5)
    try:
        clicker.start()
    except KeyboardInterrupt:
        clicker.stop()
    except Exception as e:
        print(f'Unhandled exception: {e}')
        clicker.stop()
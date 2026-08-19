import time
import pyautogui

class AutoClicker:
    def __init__(self, interval=1, duration=None):
        self.interval = interval
        self.duration = duration
        self.start_time = None

    def start_clicking(self):
        self.start_time = time.time()
        while self.duration is None or (time.time() - self.start_time < self.duration):
            pyautogui.click()
            time.sleep(self.interval)

    def stop_clicking(self):
        self.duration = 0  # setting duration to zero will stop the loop

    def change_interval(self, new_interval):
        self.interval = new_interval

    def get_clicks_per_minute(self):
        if self.duration:
            return (60 / self.interval) * (self.duration / self.interval)
        return None

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.5, duration=10)
    clicker.start_clicking()  
    print('Clicking done!')
    print('Clicks per minute:', clicker.get_clicks_per_minute())
import time
from threading import Thread

class AutoClicker:
    def __init__(self, interval=1):
        self.interval = interval
        self.running = False

    def start(self):
        self.running = True
        self._run()

    def _run(self):
        while self.running:
            self.click()
            time.sleep(self.interval)

    def click(self):
        print("Click!")  # Placeholder for actual click code

    def stop(self):
        self.running = False


def create_clicker(interval):
    return AutoClicker(interval)


def start_clicker(clicker):
    Thread(target=clicker.start).start()


def stop_clicker(clicker):
    clicker.stop()
import time
import threading

class AutoClicker:
    def __init__(self, interval=1):
        self.interval = interval
        self.running = False

    def start(self):
        self.running = True
        threading.Thread(target=self.run).start()

    def run(self):
        while self.running:
            self.click()
            time.sleep(self.interval)

    def click(self):
        print("Click!")  # Simulate clicking action

    def stop(self):
        self.running = False

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.5)
    clicker.start()
    time.sleep(5)  # Run for 5 seconds
    clicker.stop()
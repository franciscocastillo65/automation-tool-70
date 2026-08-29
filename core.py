import time
import threading
from collections import deque

class CoreModule:
    def __init__(self, target_rate=20.0):
        self.target_rate = target_rate
        self.interval = 1.0 / target_rate
        self.is_active = False
        self.worker = None
        self.total_clicks = 0
        self.sync = threading.Lock()
        self.timing_history = deque(maxlen=100)
        self.last_adjust = time.perf_counter()

    def activate(self):
        with self.sync:
            if self.is_active:
                return False
            self.is_active = True
            self.worker = threading.Thread(target=self._performance_loop)
            self.worker.daemon = True
            self.worker.start()
            return True

    def deactivate(self):
        with self.sync:
            self.is_active = False
        if self.worker is not None:
            self.worker.join(1.0)
            self.worker = None

    def _performance_loop(self):
        scheduled = time.perf_counter()
        while self.is_active:
            now = time.perf_counter()
            if now >= scheduled:
                self._do_click()
                scheduled += self.interval
                if scheduled < now:
                    scheduled = now + self.interval
                self._update_performance(now)
            else:
                wait = scheduled - now
                if wait > 0.005:
                    time.sleep(wait - 0.003)

    def _do_click(self):
        with self.sync:
            self.total_clicks += 1
        print("Click at " + str(time.perf_counter()))

    def _update_performance(self, now):
        with self.sync:
            self.timing_history.append(now)
            if len(self.timing_history) > 10 and now - self.last_adjust > 1.0:
                diffs = [self.timing_history[i+1] - self.timing_history[i] for i in range(len(self.timing_history)-1)]
                avg = sum(diffs) / len(diffs) if diffs else self.interval
                if abs(avg - self.interval) > 0.001:
                    self.interval = avg
                self.last_adjust = now

    def get_clicks(self):
        with self.sync:
            return self.total_clicks

    def set_rate(self, new_rate):
        with self.sync:
            self.target_rate = new_rate
            self.interval = 1.0 / new_rate
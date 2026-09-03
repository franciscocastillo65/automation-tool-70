import time
import threading
from queue import PriorityQueue

class ClickProcessor:
    def __init__(self):
        self.queue = PriorityQueue()
        self._running = True
        self.thread = threading.Thread(target=self._worker, daemon=True)
        self.thread.start()

    def schedule(self, delay, func, *args):
        execute_at = time.perf_counter() + delay
        self.queue.put((execute_at, func, args))

    def _worker(self):
        while self._running:
            if self.queue.empty():
                time.sleep(0.001)
                continue
            
            execute_at, func, args = self.queue.get()
            now = time.perf_counter()
            
            if now < execute_at:
                time.sleep(execute_at - now)
            
            try:
                func(*args)
            except Exception as e:
                print(f"Execution error: {e}")
            finally:
                self.queue.task_done()

    def stop(self):
        self._running = False
        self.thread.join()
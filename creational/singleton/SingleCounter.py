
import threading


class Counter:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Counter, cls).__new__(cls)
                    cls._instance._count = 0
                    cls._instance._cnt_lock = threading.Lock()
        return cls._instance
    def increment(self):
        with self._cnt_lock:
            self._count += 1
    def get_count(self):
        with self._cnt_lock:
            return self._count
        

if __name__ == "__main__":
    # After implementing, usage should look like:
    c1 = Counter()
    c2 = Counter()
    print(f"Same instance: {c1 is c2}")
    for _ in range(5):
        c1.increment()
    print(f"Count after 5 increments: {c1.get_count()}")
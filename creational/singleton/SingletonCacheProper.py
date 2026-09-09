import threading
import time


class CacheManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._cache = {}
        return cls._instance

    def put(self, key, val, ttl=0):
        expiry = time.time() + ttl if ttl > 0 else None
        with self._lock:
            self._cache[key] = (val, expiry)

    def get(self, key):
        with self._lock:
            if key not in self._cache:
                return None

            val, expiry = self._cache[key]
            if expiry is not None and expiry <= time.time():
                del self._cache[key]
                return None
            return val

    def remove(self, key):
        with self._lock:
            self._cache.pop(key, None)

    def size(self):
        now = time.time()
        with self._lock:
            return sum(
                1 for _, expiry in self._cache.values()
                if expiry is None or expiry > now
            )


if __name__ == "__main__":
    cache1 = CacheManager()
    cache2 = CacheManager()

    print("Same instance:", cache1 is cache2)

    cache1.put("key1", "value1", ttl=5)
    print("cache1 size:", cache1.size())
    print("cache2 size:", cache2.size())
    print("cache2 get key1:", cache2.get("key1"))

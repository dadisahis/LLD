import threading
import time

class CacheManager:
    def __init__(self):
        self._cache = {}
        self._lock = threading.Lock()

    def put(self, key, val, ttl=0):
        expiry = time.time()+ ttl if ttl > 0 else None
        with self._lock:
            self._cache[key] = (val, expiry)


    def get(self, key):
        with self._lock:
            if key in self._cache:
                val, expiry = self._cache[key]
                if expiry is None or expiry > time.time():
                    return val
                else:
                    del self._cache[key]
                    return None
            else:
                return None
    def remove(self, key):
        with self._lock:
            if key in self._cache:
                del self._cache[key]

    def size(self):
        now = time.time()
        with self._lock:
            return sum(1 for val, expiry in self._cache.values() if expiry is None or expiry > now)
    


cacheMgr = CacheManager()

if __name__ == "__main__":
    cache_mgr1 = cacheMgr
    cache_mgr2 = cacheMgr

    print("Same cache manager instance:", cache_mgr1 is cache_mgr2)

    cache_mgr1.put("key1", "value1", ttl=5)
    cache_mgr1.put("key2", "value2")
    print("Cache size after adding key1:", cacheMgr.size()) 
    time.sleep(6)
    print("Cache size after key1 expires:", cacheMgr.size())

    
    print("Cache size after adding key2:", cache_mgr2.size()) 
    cache_mgr2.remove("key2")
    print("Cache size after removing key2:", cache_mgr2.size())

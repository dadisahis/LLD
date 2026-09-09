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
    
# Python Modules being singleton inehereently, if here we had defined c1 = CacheManager() and c2 = CacheManager(), then 2 separate instances would  have been created and c1!=c2

# cacheMgr = CacheManager()

# if __name__ == "__main__":
#     cache_mgr1 = cacheMgr
#     cache_mgr2 = cacheMgr

#     print("Same cache manager instance:", cache_mgr1 is cache_mgr2)

#     cache_mgr1.put("key1", "value1", ttl=5)
#     cache_mgr1.put("key2", "value2")
#     print("Cache size after adding key1:", cacheMgr.size()) 
#     time.sleep(6)
#     print("Cache size after key1 expires:", cacheMgr.size())

#     cache_mgr1.put("key3", "value3")
#     print("Cache size after adding key3:", cache_mgr2.size()) 
#     cache_mgr2.remove("key3")
#     print("Cache size after removing key2:", cache_mgr2.size())


#  Proper Singleton
class SingleCache:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._cache = {}
        return cls._instance

    def put(self, key, val, ttl = 0):
        ep = time.time() + ttl if ttl > 0 else None
        with self._lock:
            self._cache[key] = (val, ep)

    def remove(self, key):
        if key in self._cache:
            with self._lock:
                del self._cache[key]

    def get(self, key):
        with self._lock:
            if key not in self._cache:
                return None
            val, ep = self._cache[key]
            if ep is not None and ep <=time.time():
                del self._cache[key]
                return None
            return val

    def size(self):
        now=time.time()
        with self._lock:
            return sum(1 for _, ep in self._cache.values() if ep is None or ep>now)


if __name__ == '__main__':
    c1 = SingleCache()
    c2 = SingleCache()
    print("Same cache manager instance:", c1 is c2)

    c1.put("key1", "value1", ttl=5)
    c1.put("key2", "value2")
    print("Cache size after adding key1:", c1.size()) 
    time.sleep(6)
    print("Cache size after key1 expires:", c1.size())

    c1.put("key3", "value3")
    print("Cache size after adding key3:", c2.size()) 
    c1.remove("key3")
    print("Cache size after removing key2:", c2.size())
from .URLRepo import URLRepo
import threading
class InMemURLRepo(URLRepo):
    def __init__(self):
        self.key_to_url_map = {}
        self.long_url_key_map = {}
        self.id_counter = 1
        self._lock = threading.Lock()
    def save(self, url):
        with self._lock:
            self.key_to_url_map[url.get_short_key()] = url
            self.long_url_key_map[url.get_long_url()] = url.get_short_key()

    def find_by_key(self, key):
        with self._lock:
            return self.key_to_url_map.get(key)
    def find_key_by_long_url(self, long_url):
        with self._lock:
            return self.long_url_key_map.get(long_url)
        
    def get_next_id(self):
        self.id_counter +=1
        return self.id_counter
    
    def exists_by_key(self, key):
        with self._lock:
            return key in self.key_to_url_map
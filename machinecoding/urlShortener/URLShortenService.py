import threading
from ShortenURL import ShortenURL
class URLShotenService:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.initialize = False
        return cls._instance
    
    def __init__(self):
        if not hasattr(self,'_initialize') or not self._initialize:
            self.url_repo = None
            self.key_gen_strat = None
            self.domain = None
            self.MAX_RETRIES = 10
            self._initialize = True

    @classmethod
    def get_instance(cls):
        return cls()
    
    def configure(self, domain, strategy, repository):
        self.domain = domain
        self.key_gen_strat = strategy
        self.url_repo = repository
    
    def shorten(self, long_url):
        exist_key = self.url_repo.find_key_by_long_url(long_url)
        if exist_key:
            return self.domain + exist_key
        
        short_key = self._gen_new_key()
        shorten_url = ShortenURL.Builder(long_url, short_key).build()
        self.url_repo.save(shorten_url)
        return self.domain + short_key
    
    def _gen_new_key(self):
        for _ in range(self.MAX_RETRIES):
            potential_key = self.key_gen_strat.gen_key(self.url_repo.get_next_id())
            if not self.url_repo.exists_by_key(potential_key):
                return potential_key
            
        raise RuntimeError("Failed to generate a unique short key after {self.MAX_RETRIES}")

    def resolve(self, short_url):
        if not short_url.startswith(self.domain):
            return None
        short_key = short_url.replace(self.domain, "")
        if self.url_repo.exists_by_key(short_key):
            short_url = self.url_repo.find_by_key(short_key)
            return short_url.get_long_url() 

        return None
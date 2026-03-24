import threading

class RateLimitService:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self.strategy = None

    @staticmethod
    def get_instance():
        if RateLimitService._instance is None:
            RateLimitService()
        return RateLimitService._instance
    
    def set_strategy(self, strategy):
        self.strategy = strategy

    def handle_req(self, user_id):
        if self.strategy.allow_request(user_id):
            print("Request from user is allowed")
        else:
            print("Request from user is not allowed")
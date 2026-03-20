import threading
class RateLimiterService:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if RateLimiterService._instance is not None:
            raise Exception("This is a SIngleton class")
        self.rate_limit_strategy = None
    
    @staticmethod
    def get_instance():
        if RateLimiterService._instance is None:
            with RateLimiterService._lock:
                if RateLimiterService._instance is None:
                    RateLimiterService._instance = RateLimiterService()
        return RateLimiterService._instance
    

    def set_rate_limiter(self, strategy):
        self.rate_limit_strategy = strategy

    def handle_req(self, user_id):
        if self.rate_limit_strategy.handle_req(user_id):
            print("Request from user is allowed")
        else:
            print("Request from user is not allowed: Rate Limit exceeded")



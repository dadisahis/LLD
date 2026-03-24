from .RateLimitStrategy import RateLimitStrategy
import time
import threading
class UserInfo:
    def __init__(self, start_time):
        self.req_count = 0
        self.start_time = start_time
        self._lock = threading.Lock()
    def reset(self, start_time):
        self.req_count = 0
        self.start_time = start_time
    
class FixedWindowStrategy(RateLimitStrategy):
    def __init__(self, capacity, window_size):
        self.capacity = capacity
        self.window_size = window_size * 1000
        self.user_map = {}
        self._lock = threading.Lock()
    
    def allow_request(self, user_id):
        curr_time = int(time.time()*1000)
        with self._lock:
            if user_id not in self.user_map:
                self.user_map[user_id] = UserInfo(curr_time)
            
            req_inf = self.user_map[user_id]
            with req_inf._lock:
                if curr_time - req_inf.start_time > self.window_size:
                    req_inf.reset(curr_time)
                
                if req_inf.req_count < self.capacity:
                    req_inf.req_count+=1
                    return True
                else: return False
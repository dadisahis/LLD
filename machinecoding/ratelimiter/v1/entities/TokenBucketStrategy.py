from .RateLimitStrategy import RateLimitStrategy
from typing import Dict
import threading
import time

class TokenBucketInfo:
    def __init__(self, capacity, refill_rt_per_sec, curr_time_ms):
        self.capacity = capacity
        self.refill_rt_per_sec = refill_rt_per_sec
        self.tokens = capacity
        self.last_refill_ts = curr_time_ms
        self._lock = threading.Lock()
    
    def refill(self, current_time):
        elapse_time = current_time - self.last_refill_ts
        tokens_to_add = int((elapse_time)/1000) * self.refill_rt_per_sec

        if tokens_to_add > 0:
            self.tokens = min(self.capacity, self.tokens + tokens_to_add)
            self.last_refill_ts = current_time
    

class TokenBucketStrategy(RateLimitStrategy):
    def __init__(self, capacity, refill_rt_per_sec):
        self.capacity = capacity
        self.refill_rt_per_sec = refill_rt_per_sec
        self.user_map:Dict['str', 'TokenBucketInfo'] = {}
        self._lock = threading.Lock()
    
    def handle_req(self, user_id):
        curr_time = int(time.time()) * 1000
        with self._lock:
            if user_id not in self.user_map:
                self.user_map[user_id] = TokenBucketInfo(self.capacity, self.refill_rt_per_sec, curr_time)
            
            token_info = self.user_map[user_id]
            with token_info._lock:
                token_info.refill(curr_time)
                if token_info.tokens > 0:
                    token_info.tokens -=1
                    return True
                else:
                    return False
from .RateLimitStrategy import RateLimitStrategy
from typing import Dict
import threading
import time
class UserRequestInfo:
    def __init__(self, windowStart):
        self.request_count = 0
        self.windowStart = windowStart
        self._lock = threading.Lock()

    def reset(self, windowStart):
        self.request_count = 0
        self.windowStart = windowStart

class FixedWindowStrategy(RateLimitStrategy):
    def __init__(self, max_req, window_size):
        self.max_req = max_req
        self.winow_size_ms = window_size*1000
        self.usr_req_map: Dict[str, 'UserRequestInfo'] = {}
        self._lock = threading.Lock()


    def handle_req(self, user_id):
        curr_time = int(time.time()*1000)
        with self._lock:
            if user_id not in self.usr_req_map:
                self.usr_req_map[user_id] = UserRequestInfo(curr_time)
            
            req_info = self.usr_req_map[user_id]
            with req_info._lock:
                if curr_time - req_info.windowStart >= self.winow_size_ms:
                    req_info.reset(curr_time)
                if req_info.request_count < self.max_req:
                    req_info.request_count +=1
                    return True
                else:
                    return False
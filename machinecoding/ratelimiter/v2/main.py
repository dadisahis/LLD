from entities.FixedWindowStrategy import FixedWindowStrategy
from RateLimitService import RateLimitService
from concurrent.futures import ThreadPoolExecutor
import time
class Democlass:
    @staticmethod
    def main():
        user_id = "123"
        print("---------Fixed Window Demo-----------")
        Democlass.run_fixed_window(user_id=user_id)
    
    @staticmethod
    def run_fixed_window(user_id):
        max_req = 5
        window_size = 10
        rate_limiter = FixedWindowStrategy(max_req, window_size)
        service = RateLimitService.get_instance()
        service.set_strategy(rate_limiter)

        with ThreadPoolExecutor(max_workers=3) as workers:
            for i in range(10):
                workers.submit(service.handle_req, user_id)
                try:
                    time.sleep(0.5)
                except KeyboardInterrupt:
                    break

if __name__ == '__main__':
    Democlass.main()
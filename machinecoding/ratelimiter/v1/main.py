from entities.FixedWindowStrategy import FixedWindowStrategy
from entities.TokenBucketStrategy import TokenBucketStrategy
from RateLimiterService import RateLimiterService
from concurrent.futures import ThreadPoolExecutor
import time
class DemoClass:
    @staticmethod
    def main():
        user_id ="ai123"
        print('-----Fixed Window Demo-----')
        DemoClass.run_fixed_window(user_id)

        print('-----Token Bucket Demo-----')
        DemoClass.run_token_bucket(user_id)

    @staticmethod
    def run_fixed_window(user_id):
        max_req = 5
        window_size =  10

        rate_limiter = FixedWindowStrategy(max_req,window_size)
        service = RateLimiterService.get_instance()
        service.set_rate_limiter(rate_limiter)

        with ThreadPoolExecutor(max_workers= 3) as workers:
            for i in range(10):
                workers.submit(service.handle_req, user_id)
                try:
                    time.sleep(0.5)
                except KeyboardInterrupt:
                    break

    @staticmethod
    def run_token_bucket(user_id):
        capacity = 5
        refilll_rt=1

        rate_limiter = TokenBucketStrategy(capacity,refilll_rt)
        service = RateLimiterService.get_instance()
        service.set_rate_limiter(rate_limiter)

        with ThreadPoolExecutor(max_workers= 3) as workers:
            for i in range(10):
                workers.submit(service.handle_req, user_id)
                try:
                    time.sleep(0.3)
                except KeyboardInterrupt:
                    break

if __name__ == '__main__':
    DemoClass.main()
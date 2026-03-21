from .NotificationGateway import *
import time
class RetryDecorator(NotificationGateway):
    def __init__(self, gateway: NotificationGateway, max_retries, retry_delay):
        self.gateway = gateway
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.retry_multiple = 2

    def send(self, notification):
        attempt = 0
        while attempt<=self.max_retries:
            if attempt > 0:
                print("Retrying to send notification")
            try: 
                self.gateway.send(notification)
                return
            except Exception as e:
                print("Failed to send notification")
                attempt +=1
                if attempt >self.max_retries:
                    print(str(e))
                    raise Exception("Failed to send after Max Retries reached")
                time.sleep((self.retry_delay /1000)* self.retry_multiple)
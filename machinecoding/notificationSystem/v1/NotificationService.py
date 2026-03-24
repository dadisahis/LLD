from concurrent.futures import ThreadPoolExecutor
from entities.Notification import Notification
from entities.RetryDecorator import RetryDecorator
from entities.NotificationFactory import NotifFactory
class NotificationService:
    def __init__(self, pool_size):
        self.workers = ThreadPoolExecutor(max_workers=pool_size)
    
    def send_notif(self, notification: Notification):
        def send_task():
            gateway = RetryDecorator(NotifFactory.create_gateway(notification_type=notification.get_type()),
                                          5,
                                          1000)
            try:
                gateway.send(notification)
            except Exception as e:
                print(f"Exception while sending notification: {e}")
        self.workers.submit(send_task)
    def shutdown(self):
        self.workers.shutdown()
                
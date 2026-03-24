from concurrent.futures import ThreadPoolExecutor
from entities.NotificationFactory import NotificationFactory
from entities.Notification import Notification
class NotifService:
    def __init__(self, pool_size):
        self.workers = ThreadPoolExecutor(max_workers=pool_size)

    def send_notif(self, notification: Notification):
        def send_task():
            gateway = NotificationFactory().get_factory(type=notification.type)
            try:
                gateway.send(notification)
            except Exception as e:
                print(str(e))
                raise Exception("Error Occured")

        self.workers.submit(send_task)
    def shutdown(self, wait=True):
        self.workers.shutdown(wait=wait)        
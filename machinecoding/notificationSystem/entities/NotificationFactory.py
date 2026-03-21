from typing import Dict
from .NotificationType import NotificationType
from  .NotificationGateway import *
class NotifFactory:
    _gatway_mp:Dict[NotificationType, NotificationGateway] = {}

    @classmethod
    def create_gateway(self, notification_type: NotificationType):
       self._gatway_mp = {
           NotificationType.EMAIL : EmailGateway(),
           NotificationType.SMS : SMSGateway(),
           NotificationType.PUSH : PushGateway()
       }
       if notification_type not in self._gatway_mp:
           return None
       return self._gatway_mp[notification_type]
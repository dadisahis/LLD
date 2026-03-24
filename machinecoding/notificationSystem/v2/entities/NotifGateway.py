from abc import ABC, abstractmethod
from .Notification import Notification

class NotifGateway(ABC):
    @abstractmethod
    def send(self, notification: Notification):
        pass

class EmailGateway(NotifGateway):
    def send(self, notification: Notification):
        email = notification.recipient.email
        if email is None:
            raise Exception("Email not found")
        
        print("Email Message")
        print(f"To: {email}")
        print(f"Subject: {notification.subject}")
        print(f"Message: {notification.message}")


class SMSGateway(NotifGateway):
    def send(self, notification: Notification):
        messageToken = notification.recipient.messageToken
        if messageToken is None:
            raise Exception("Email not found")
        
        print("SMS Message")
        print(f"To: {messageToken}")
        print(f"Message: {notification.message}")








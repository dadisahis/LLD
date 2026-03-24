from abc import ABC, abstractmethod
from .Notification import Notification
class NotificationGateway(ABC):
    @abstractmethod
    def send(self, notification: 'Notification'):
        pass



class EmailGateway(NotificationGateway):
    def send(self, notification: 'Notification'):
        email = notification.get_recipient().get_email()
        if email is None:
            raise ValueError("No Email address found")
        
        print(f"Email Message sent to {email} , subject: {notification.get_subject()}, message: {notification.get_message()}")
    

class SMSGateway(NotificationGateway):
    def send(self, notification: 'Notification'):
        phoneNumber = notification.get_recipient().get_phone_no()
        if phoneNumber is None:
            raise ValueError("No Phone number found")
        print(f"SMS Message sent to {phoneNumber} , message: {notification.get_message()}")
    

class PushGateway(NotificationGateway):
    def send(self, notification: 'Notification'):
        pushToken = notification.get_recipient().get_token()
        if pushToken is None:
            raise ValueError("No device token found")
        print(f"Push Notification sent to {pushToken} , message: {notification.get_message()}")
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class SMSNotificattion(Notification):
    def send(self, message):
        return "SMS sent: " + message
    
class EmailNotification(Notification):
    def send(self, message):
        return "Email sent: " + message
    

class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self):
        pass

    def send_notification(self, message):
        ntf = self.create_notification()
        return ntf.send(message)
    

class SMSNotificationCreator(NotificationFactory):
    def create_notification(self):
        return SMSNotificattion()
    
class EmailNotificationCreator(NotificationFactory):
    def create_notification(self):
        return EmailNotification()
    


if __name__ == "__main__":
    sms_creator = SMSNotificationCreator()
    email_creator = EmailNotificationCreator()

    print(sms_creator.send_notification("Hello via SMS!"))
    print(email_creator.send_notification("Hello via Email!"))


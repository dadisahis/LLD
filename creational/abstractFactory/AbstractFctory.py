from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def set_content(self, to, message):
        pass    

class Sender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailMessage(Message):
    def set_content(self, to, message):
        self.to = to
        self.message = message
    def format_message(self):
        return f"Email to {self.to}: {self.message}"

class SMSMessage(Message):
    def set_content(self, to, message):
        self.to = to
        self.message = message
    def format_message(self):
        return f"SMS to {self.to}: {self.message}"
    

class EmailSender(Sender):
    def send(self, message):
        if isinstance(message, EmailMessage):
            print("Sending email:", message.format_message())
        else:
            raise ValueError("Invalid message type for EmailSender")

class SMSSender(Sender):
    def send(self, message):
        if isinstance(message, SMSMessage):
            print("Sending SMS:", message.format_message())
        else:
            raise ValueError("Invalid message type for SMSSender")
        

class EmailFactory:
    def create_message(self):
        return EmailMessage()
    def create_sender(self):
        return EmailSender()

class SMSFactory:
    def create_message(self):
        return SMSMessage()
    def create_sender(self):
        return SMSSender()
    

class NotificationService:
    def __init__(self, factory):
        self.factory=factory
    
    def notify(self, to, message):
        msg = self.factory.create_message()
        msg.set_content(to, message)
        sender = self.factory.create_sender()
        sender.send(msg)


if __name__ == "__main__":
    email_service = NotificationService(EmailFactory())
    sms_service = NotificationService(SMSFactory())

    email_service.notify("adi@mail.com", "Hello via Email!")
    sms_service.notify("1234567890", "Hello via SMS!")
    
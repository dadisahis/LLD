from uuid import uuid4
from .NotificationType import NotificationType
from .Recipient import Recipient
class Notification:
    def __init__(self, builer: 'Builder'):
        self.id = str(uuid4())
        self.subject = builer.subject
        self.message = builer.message
        self.recipient = builer.recipient
        self.type = builer.type

    def get_id(self):
        return self.id
    def get_subject(self):
        return self.subject
    def get_message(self):
        return self.message
    def get_type(self):
        return self.type
    def get_recipient(self):
        return self.recipient

    class Builder:
        def __init__(self, recipient: Recipient, type: NotificationType):
            self.recipient = recipient
            self.subject = None
            self.message = None
            self.type = type

        def set_subject(self, subject):
            self.subject = subject
            return self
        
        def set_message(self, message):
            self.message = message
            return self
        
        def build(self):
            return Notification(self)
        
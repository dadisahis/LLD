from .enums import *
from .Recipient import Recipient
class Notification:
    def __init__(self, builder: 'Builder'):
        self.type = builder.type
        self.subject = builder.subject
        self.message = builder.message
        self.recipient = builder.recipient


    class Builder:
        def __init__(self, type: NotifType, recipient: Recipient):
            self.type = type
            self.subject = None
            self.message=None
            self.recipient = recipient

        def set_subject(self, subject):
            self.subject = subject
            return self
        def set_message(self, message):
            self.message = message
            return self
        def build(self):
            return Notification(self)            
from .enums import NotifType
from .NotifGateway import *
class NotificationFactory:
    _mp = {}

    @classmethod
    def get_factory(cls, type: NotifType):
        if not hasattr(cls, '_mp') or not cls._mp:    
            cls._mp = {
                NotifType.EMAIL : EmailGateway(),
                NotifType.SMS : SMSGateway()
            }
        if type not in cls._mp:
            raise Exception("Invalid Type")
        return cls._mp.get(type)
    

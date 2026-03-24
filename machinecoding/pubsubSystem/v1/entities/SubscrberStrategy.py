from abc import ABC, abstractmethod
from .Message import Message
class Subcsriber:
    @abstractmethod
    def onMessage(self, message:'Message'):
        pass


class AlertSubscriber(Subcsriber):
    def __init__(self, id):
        self._id = id
        
    def get_id(self):
        return self._id
    def onMessage(self, message):
        print(f"Alert Message: id:{self.get_id()}, payload: {message.get_payload()}")


class NewsSubscriber(Subcsriber):
    def __init__(self, id):
        self._id = id
    def get_id(self):
        return self._id
    def onMessage(self, message):
        print(f"News Message: id:{self.get_id()}, payload: {message.get_payload()}")
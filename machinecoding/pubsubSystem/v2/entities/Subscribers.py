from abc import ABC, abstractmethod
from .Message import Message

class Subscriber(ABC):
    @abstractmethod
    def on_message(self, message):
        pass
    

class AdSubscriber(Subscriber):
    def __init__(self,id):
        self.id = id
    def on_message(self, message: Message):
        print(f"Ad Subscriber {self.id} running with payload: {message.get_payload()}")
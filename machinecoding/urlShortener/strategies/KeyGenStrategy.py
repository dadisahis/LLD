from abc import ABC, abstractmethod

class KeyGenStrategy(ABC):
    @abstractmethod
    def gen_key(self, id):
        pass
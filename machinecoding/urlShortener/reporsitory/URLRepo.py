from abc import ABC, abstractmethod

class URLRepo(ABC):
    @abstractmethod
    def get_next_id(self):
        pass

    @abstractmethod
    def save(self, shortURL):
        pass

    @abstractmethod
    def find_by_key(self, key):
        pass

    @abstractmethod
    def find_key_by_long_url(self, long_url):
        pass
    
    @abstractmethod
    def exists_by_key(self, key):
        pass
from abc import ABC, abstractmethod
class RateLimitStrategy(ABC):
    @abstractmethod
    def allow_request(self):
        pass
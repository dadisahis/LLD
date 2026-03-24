from abc import ABC, abstractmethod

class RateLimitStrategy(ABC):
    @abstractmethod
    def handle_req(self, user_id: str):
        pass

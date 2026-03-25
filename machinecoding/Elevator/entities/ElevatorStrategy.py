from abc import ABC, abstractmethod

class ElevatorStrategy(ABC):
    @abstractmethod
    def move_elevator(self, targets):
        pass


class SimpleStrategy(ElevatorStrategy):
    def move_elevator(self, current_floor, targets):
        if not targets:
            return current_floor
        return targets.pop(0)
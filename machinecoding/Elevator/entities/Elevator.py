from enum import Enum
import heapq
from .Request import Request
class Direction:
    DOWN="Down"
    UP="Up"
    IDLE="Idle"

class Elevator:
    def __init__(self, id, strategy ,current_floor=0):
        self.id = id
        self.strategy = strategy
        self.current_floor = current_floor
        self.targets = []
        self.direction = Direction.IDLE
    def add_request(self, request: Request):
        self.targets.append(request.source)
        self.targets.append(request.destination)

    def move(self):
        next_floor = self.strategy.move_elevator(self.current_floor, self.targets)
        if self.current_floor > next_floor:
            self.direction = Direction.DOWN
        elif self.current_floor < next_floor:
            self.direction = Direction.UP
        else:
            self.direction = Direction.IDLE

        # Prevent "up 0 to 0" when there is no movement
        if self.direction != Direction.IDLE:
            print(f"Lift {self.id} moving {self.direction} from {self.current_floor} to {next_floor}")
        else:
            print(f"Lift {self.id} idle at {self.current_floor}")

        self.current_floor = next_floor
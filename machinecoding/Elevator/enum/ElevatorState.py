from enum import Enum

class Elevator(Enum):
    IDLE="IDLE"
    MOVING="MOVING"
    DOOR_OPEN="DOOR_OPEN"
    OUT_OF_SERVICE="OUT_OF_SERVICE"
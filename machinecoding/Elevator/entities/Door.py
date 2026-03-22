from ..enum.DoorState import DoorState 
class Door:
    def __init__(self):
        self._state: DoorState = DoorState.CLOSED.value

    def open(self):
        self._state = DoorState.OPEN.value
        return
    def close(self):
        self._state = DoorState.CLOSED.value
        return
    def isOpen(self):
        return self._state == DoorState.OPEN.value
    

    
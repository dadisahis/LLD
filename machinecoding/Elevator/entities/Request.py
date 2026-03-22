from ..enum.Direction import Direction
from ..enum.RequestState import RequestState
from datetime import datetime
class Request:
    def __init__(self, floor:int ,direction:Direction ,type:RequestState ):
        self._floor = floor
        self._direction = direction
        self._type = type
        self._timestamp = datetime.now()
    def get_floor(self):
        return self._floor
    def get_direction(self):
        return self._floor
    def get_type(self):
        return self._type
    
    def get_timestamp(self):
        return self._timestamp
    

    
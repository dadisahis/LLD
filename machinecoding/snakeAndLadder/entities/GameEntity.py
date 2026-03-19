from abc import ABC, abstractmethod
class GameEntity(ABC):
    def __init__(self, start:int , end: int):
        self._start = start
        self._end = end

    def get_start(self):
        return self._start
    def get_end(self):
        return self._end



class Snake(GameEntity):
    def __init__(self, start, end):
        if(start < end):
            raise ValueError("Snake start value cannot be lower than end value")
        super().__init__(start, end)
        

class Ladder(GameEntity):
    def __init__(self, start, end):
        if(start > end):
            raise ValueError("Laddder start value cannot be lower than end value")
        super().__init__(start, end)
        


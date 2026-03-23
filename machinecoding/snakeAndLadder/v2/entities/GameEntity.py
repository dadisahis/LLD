from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def get_start(self):
        return self._start
    def get_end(self):
        return self._end
    

class Snake(Entity):
    def __init__(self, start, end):
        if start < end:
            raise ValueError("Snake cannot have a start smaller than end")
        super().__init__(start, end)

class Ladder(Entity):
    def __init__(self, start, end):
        if start > end:
            raise ValueError("Ladder cannot have a start greater than end")
        super().__init__(start, end)



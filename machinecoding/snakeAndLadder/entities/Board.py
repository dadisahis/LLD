from typing import List
from .GameEntity import GameEntity
class Board:
    def __init__(self, size, entity: List['GameEntity'] = []):
        self._size = size
        self.snake_ladders = {}
        if len(entity)>0:
            for ent in entity:
                self.snake_ladders[ent.get_start()] = ent.get_end()

    def getSize(self) -> int:
        return self._size
    
    def get_final_position(self, pos) -> int:
        return self.snake_ladders.get(pos, pos)
    
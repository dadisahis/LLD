class Board:
    def __init__(self, size, entities):
        self._size = size
        self.snake_ladders = {}
        if len(entities) > 0:
            for ent in entities:
                self.snake_ladders[ent.get_start()] = ent.get_end()
    def get_size(self):
        return self._size
    
    def get_final_pos(self, pos):
        return self.snake_ladders.get(pos, pos)
    




        
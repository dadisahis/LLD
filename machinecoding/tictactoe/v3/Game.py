from entities import *
from collections import *
class Game:
    def __init__(self, size, players):
        self.board = Board(size)
        self.player_q = deque(players)
        self.state = GameState.PLAYIN
        self.rows = [0]*size
        self.cols = [0]*size
        self.diag = 0
        self.anti = 0
    

    def make_move(self, row, col, symbol):
        self.board.place_symbol(row, col, symbol)
        val = 1 if symbol == Symbol.X else -1

        size = self.board.size
        self.rows[row] +=val
        self.cols[col] +=val
        
        if row == col:
            self.diag += val
        if row+col == size  - 1:
            self.anti += val

        if  abs(self.rows[row]) == size or abs(self.cols[col])==size or abs(self.diag)==size or abs(self.anti)==size:
            self.state = GameState.WIN  
            return self.state
        
        if self.board.is_full():
            self.state = GameState.DRAW
            return self.state
        self.state == GameState.PLAYIN
        return self.state
        
        
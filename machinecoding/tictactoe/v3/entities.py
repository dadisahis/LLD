from enum import Enum

class Symbol: 
    X='X'
    O='O'
class GameState:
    WIN="WIN"
    DRAW="DRAW"
    PLAYIN="PLAYING"
class Player:
    def __init__(self,name, symbol: Symbol):
        self.name = name
        self.symbol = symbol

class Board:
    def __init__(self, size):
        self.size = size
        self._board = [[None for _ in range(size)] for _ in range(size)]

    def place_symbol(self, row, col, symbol):
        if row<0 or row >= self.size or col < 0 or col >= self.size:
            print("Invalid entry")
            return False
        if self._board[row][col] is not None:
            print("Cell is already occupied")
            return False

        self._board[row][col] = symbol
        return True
    
    def print_board(self):
        for i in range(self.size):
            row = [cell if cell is not None else " " for cell in self._board[i]]
            print(" | ".join(row))
            if i < self.size-1:
                print("-" * (self.size *2 - 1))

    def is_full(self):
        return all(cell is not None for row in self._board for cell in row)        

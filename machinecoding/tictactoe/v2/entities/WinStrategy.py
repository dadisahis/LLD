from abc import ABC, abstractmethod

class WinStrategy(ABC):
    @abstractmethod
    def check_win(self, symbol):
        pass


class WinWDiag(WinStrategy):
    def __init__(self, board):
        self.board = board

    def check_win(self, symbol):
        # check row
        for col in self.board.board:
            if all(cell == symbol for cell in col):
                return True
            
        for col in range(self.board.size):
            if all(self.board.board[row][col] == symbol for row in range(self.board.size)):
                return True
        if all(self.board.board[i][i] == symbol for i in range(self.board.size)):
            return True
        if all(self.board.board[i][self.board.size - i -1] == symbol for i in range(self.board.size)):
            return True
        return False
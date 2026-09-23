'''
Requirements
1. 3x3 Board
2. 2 players X and O
Alternate Turns
Winning Condition, one should occupy either a row, a col or one of the diagonals else its a draw
Game ends after a win or Draw

Use Cases
1. Create game
2. Register Users
3. Make Move
4. Validate Move
5. Check win
6. Check Draw
7. Get current game status and board

Entities
1. Game - Class
    - orchestrator
    - coordinate players, current player, board, game status, make moves, check winner , switch turns
2. Board - Class
    - cells, whether cell is empty, whether move is valid, place a symbol, is board full, 
3. Player - Class
    - name,symbol
4. GameStatus - Enum
5. Symbol - Enum
'''
from enum import Enum
from collections import deque

class Symbol(Enum):
    X="X"
    O="O"

class GameStatus(Enum):
    INIT="0"
    IN_PROGRESS = "1"
    END = "2"

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Board:
    def __init__(self, size=3):
        self.size = size
        self.board  = [[None for i in range(self.size)] for j in range(self.size)]

    def place_symbol(self, symbol: Symbol, row: int, col: int):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            raise ValueError("Move Out of Bounds")
        if  self.board[row][col] != None:
            raise ValueError("Invalid Move, Position already occupied")
        self.board[row][col] = symbol

    def is_full(self):
        for row in self.board:
            if None in row:
                return False
        return True
    def print_board(self):
        for row in self.board:
            print( " | ".join(cell.value if cell else "-" for cell in row))
            print("-" * (self.size* 4 - 1))

class Game:
    def __init__(self, players: list[Player], n:int =3):
        self.players = deque(players)
        self.board = Board(n)
        self.status = GameStatus.INIT
        self.winner = None #Either symbol or draw

    def update_status(self, status: GameStatus):
        self.status = status

    def check_winner(self, symbol: Symbol, row:int, col:int):
        if all(self.board.board[row][c]==symbol for c in range(self.board.size)):
            return True
        if all(self.board.board[r][col]==symbol for r in range(self.board.size)):
            return True
        #Diag
        if row==col:
            if all(self.board.board[i][i]==symbol for i in range(self.board.size)):
                return True
        #anti diag
        if row+col == self.board.size - 1:
            if all(self.board.board[i][self.board.size - 1 -i]==symbol for i in range(self.board.size)):
                    return True
        return False

    def make_move(self, symbol: Symbol, row:int, col:int):
        if self.status!=GameStatus.IN_PROGRESS:
            raise ValueError("Game has ended")
        self.board.place_symbol(symbol, row, col)
        if self.check_winner(symbol, row, col):
            self.status = GameStatus.END
            self.winner = symbol.value
            return
        if self.board.is_full():
            self.status = GameStatus.END
            self.winner = "DRAW"
            return


        

def main():
    game = Game([Player("Adi", Symbol.X),Player("Anu", Symbol.O)], 3)
    game.update_status(GameStatus.IN_PROGRESS)
    while game.status == GameStatus.IN_PROGRESS:
        game.board.print_board()
        curr_pl = game.players.popleft()
        try:
            print(f"{curr_pl.name}: {curr_pl.symbol}, enter the position you want to place your symbol")
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            game.make_move(curr_pl.symbol, row, col)
            if game.status == GameStatus.END:
                if game.status !="DRAW":
                    print(f"Congratulations, {game.winner} has won the game")
                else: 
                    print("Game has ended in a draw")
                break
            game.players.append(curr_pl)
        except Exception as e:
            print(e)
            game.players.appendleft(curr_pl)
if __name__ == "__main__":
    main()



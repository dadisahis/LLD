
from models.Player import Player
from models.Board import Board
from models.PieceType import PieceType, PieceX, PieceO
from collections import deque


class TicTacToe:
    def __init__(self, size: int):  
        self.players_queue = deque()
        self._initializeGame(size)
        

    def _initializeGame(self, size: int):
        player1 = input("Enter name for Player 1: ")
        player2 = input("Enter name for Player 2: ")

        player1 = Player(player1, PieceX().__str__())
        player2 = Player(player2, PieceO().__str__())
        self.players_queue.append(player1)
        self.players_queue.append(player2)
        self.board = Board(size) 


    def startGame(self):
        noWinner = True
        while noWinner:
            curr_player = self.players_queue.popleft()
            self.board.print_board()
            
            print(f"{curr_player.get_name()}'s turn. Your piece is {curr_player.get_peice()}")
            row = int(input("Enter row: ")) 
            col = int(input("Enter column: "))
            # Validate move and update board
            is_added_successfully = self.board.place_piece(row, col, curr_player.get_peice())
            if not is_added_successfully:
                print("Invalid move. Try again.")
                self.players_queue.appendleft(curr_player)
                continue
            self.players_queue.append(curr_player)
            isWinner = self.board.check_winner(curr_player.get_peice())
            if isWinner:
                self.board.print_board()
                print(f"{curr_player.get_name()} wins!")
                noWinner = False

            if self.board.get_free_cells() == []:
                print("It's a draw!")
                break

    

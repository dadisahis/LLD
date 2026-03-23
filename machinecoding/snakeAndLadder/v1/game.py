from collections import deque
from entities.Board import Board
from entities.Dice import Dice
from entities.User import User
from enums import GameStatus
class Game:
    def __init__(self, builder: 'GameBuilder'):
        self.board = builder.board
        self.players = builder.players
        self.dice = builder.dice
        self.status = GameStatus.GameStatus.NOT_STARTED
        self.winner = None
    
    def play(self):
        if len(self.players)<2:
            raise ValueError("There cannot be less than 2 players")
        
        self.status = GameStatus.GameStatus.RUNNING
        print("-----------------Game Started-------------------")

        while self.status == GameStatus.GameStatus.RUNNING:
            curr_player = self.players.popleft()
            self.apply_turn(curr_player)
            if self.status == GameStatus.GameStatus.RUNNING:
                self.players.append(curr_player)

        print("Game Finished")
        if self.winner is not None:
            print(f"Congratulations! The winner is {self.winner.get_name()}")
    
    def apply_turn(self, curr_player):
        roll = self.dice.roll_dice()
        print(f"{curr_player.get_name()} rolled {roll}")

        curr_pos = curr_player.get_position()
        next_position = curr_pos + roll
        if next_position > self.board.getSize():
            print("Skip turn")
            return
        if next_position == self.board.getSize():
            self.winner = curr_player
            self.status = GameStatus.GameStatus.FINISHED
            return
        
        
        #handle case if you incur a snake or a ladder
        final_pos = self.board.get_final_position(next_position)
        if final_pos > next_position:
            print(f"Wohoo! You have found a ladder, now you have moved from {next_position} to {final_pos}")
        elif final_pos < next_position:
            print(f"Oooops! You got bit by a snake, now you have dropped from {next_position} to {final_pos}")
        else:
            print(f"Player moves from {curr_pos} to {final_pos}")
        curr_player.set_position(final_pos) 

        if roll == 6:
            print(f"{curr_player.get_name()} rolled a 6 and gets another turn!")
            self.apply_turn(curr_player)
        return
    class GameBuilder:
        def __init__(self):
            self.board = None
            self.players = None
            self.dice = None
        
        def set_board(self, size: int, entity: 'Board'):
            self.board = Board(size, entity)
            return self
        def set_players(self, player_names):
            self.players = deque()
            for nm in player_names:
                self.players.append(User(nm))

            return self
        def set_dice(self, minVal, maxVal):
            self.dice = Dice(minVal, maxVal)
            return self

        def build(self):
            return Game(self)
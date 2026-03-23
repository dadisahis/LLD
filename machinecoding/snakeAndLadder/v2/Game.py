from collections import deque
from entities.Board  import *
from entities.Dice  import *
from entities.Status  import *
from entities.GameEntity  import *
from entities.Player  import *
class Game:
    def __init__(self, builer: 'Builder'):
        self.board = builer.board
        self.dice = builer.dice
        self.players = builer.players
        self.winner = None
        self.status = Status.NOT_STARTED.value
    
    def play(self):
        if len(self.players)< 2:
            raise ValueError("Players cannot be less than 2")
        self.status = Status.PLAYING.value
        print(f'-------------Game Started------------')
        while self.status == Status.PLAYING.value:
            curr_player = self.players.popleft()
            self.apply_turn(curr_player)
            if self.status == Status.PLAYING.value:
                self.players.append(curr_player)
        
        if self.winner:
            print(f"Congratulations to the winner: {self.winner.get_name()}")

    def apply_turn(self, curr_player):
        roll = self.dice.roll_dice()
        print(f"{curr_player.get_name()} rolledd {roll}")

        curr_pos =  curr_player.get_position()
        next_pos= curr_pos + roll
        if next_pos > self.board.get_size():
            print("Skip turn")
            return
        if next_pos == self.board.get_size():
            self.winner = curr_player
            self.status = Status.FINISHED.value
            return
        final_pos = self.board.get_final_pos(next_pos)
        if final_pos > next_pos:
            print(f"You have encountered a ladder. Moving up from {next_pos} to {final_pos}")
        elif final_pos < next_pos:
            print(f"You have encountered a snake. Moving down from {next_pos} to {final_pos}")
        else:
            print(f"Moving to {final_pos}")
        curr_player.set_position(final_pos)
        return

    class Builder:
        def __init__(self):
            self.board = None
            self.players = deque()
            self.dice = None
        

        def set_board(self, size, entties):
            self.board = Board(size, entties)
            return self
        def set_players(self, players):
            for name in players:
                self.players.append(Player(name))
            return self
        def set_dice(self, minVal, maxVal):
            self.dice = Dice(minVal, maxVal)
            return self

        def build(self):
            return Game(self)
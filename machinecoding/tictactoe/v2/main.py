from entities.Player import Player
from entities.Enums import *
from entities.Board import *
from entities.WinStrategy import *
from GameService import GameService
def main():
    players = [Player("Adi", Symbol.X), Player("Anu", Symbol.O)]
    board = Board(3)
    strategy = WinWDiag(board)

    game_service = GameService(players=players, board=board, strategy=strategy, total_games=3)
    game_service.play()


if __name__ == '__main__':
    main()
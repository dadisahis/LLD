from Game import *


def main():
    game_entities = [
            Snake(17, 7), Snake(54, 34),
            Snake(62, 19), Snake(98, 79),
            Ladder(3, 38), Ladder(24, 33),
            Ladder(42, 93), Ladder(72, 84)
        ]
    game = Game.Builder().set_board(100,game_entities).set_players(['adi', 'anu']).set_dice(1,6).build()
    game.play()


if __name__ == '__main__':
    main()
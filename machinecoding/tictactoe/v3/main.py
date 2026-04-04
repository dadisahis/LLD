from entities import *
from Game import Game
def main():
    size = 3
    p1 = Player("Adi", Symbol.X)
    p2 = Player("Anu", Symbol.O)    
    game = Game(size, [p1, p2])

    while True:
        game.board.print_board()
        player = game.player_q.popleft()
        try: 
            print(f"Player {player.name}'s turn")
            row, col = map(int, input("Enter row and col").split())
            result = game.make_move(row, col, player.symbol)
            if result == GameState.WIN:
                print(f"Player {player.name}'s Wins")
                break
            elif result == GameState.DRAW:
                print("Games endedd in a draw")
                break
            game.player_q.append(player)
        except Exception as e:
            print("Error", str(e))
            game.player_q.append(player)  # Put player back on invalid move

if __name__ == '__main__':
    main()
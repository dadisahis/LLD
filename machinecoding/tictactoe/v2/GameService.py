from entities.Board import *
class GameService:
    def __init__(self, board, players, strategy, total_games):
        self.board = board
        self.players = players
        self.strategy = strategy
        self.total_games= total_games
        self.score_board = ScoreBoard([player.name for player in self.players])

    def play(self):
        games_played = 0
        while games_played < self.total_games:
            curr_player = self.players.pop(0)
            symbol = curr_player.symbol.value

            try:
                row, col = map(int, input(f"{curr_player.name}'s move:").split())
                self.board.place_symbol(row, col, symbol)
                self.board.print_board()
                is_win = self.strategy.check_win(symbol)
                if is_win:
                    print(f"{curr_player.name} wins game number: {games_played+1}")
                    self.score_board.update_score(curr_player.name)
                    games_played+=1
                    self.score_board.print_scoreboard()
                    self.board.reset_board()
                else:
                    draw =self.board.check_draw()
                    if draw:
                        self.score_board.update_score(curr_player.name)
                        games_played+=1
                        self.score_board.print_scoreboard()
                        self.board.reset_board()
                self.players.append(curr_player)
            except Exception as e:
                print(e)

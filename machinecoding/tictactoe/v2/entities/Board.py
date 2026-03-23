class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None for i in range(size)]for j in range(size)]

    def reset_board(self):
        self.board = [[None for i in range(self.size)]for j in range(self.size)]
        return

    def place_symbol(self, row, col, symbol):
        if row > self.size or row <0 or col > self.size or col <0:
            print("Invalid move")
            return False
        if self.board[row][col] == None:
            self.board[row][col] = symbol
            return True
        else:
            print("Invalid move!")
            return False
    def check_draw(self):
        for col in self.board:
            for cell in col:
                if cell is None:
                    return False
        return True
    def print_board(self):
        for col in range(self.size):
            print('|'.join([row if row is not None else ' ' for row in self.board[col] ]))
            if col < self.size -1:
                print('_' * (self.size*2 - 1))


class ScoreBoard:
    def __init__(self, player_list):
        self.map = {}
        for pl in player_list:
            self.map[pl] = 0

        self.map['draw'] = 0

    def update_score(self, name):
        self.map[name]+=1
        return

    def print_scoreboard(self):
        for k,v in self.map.items():
            print(f"Player {k} has {v} wins" if k != 'draw' else f"There has been {v} draws")

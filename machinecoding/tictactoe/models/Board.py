class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)] 


    def print_board(self):
        for row in self.board:
            print(" | ".join([str(cell) if cell else " " for cell in row]))
            print("-" * (self.size * 4 - 1))

    def place_piece(self, row: int, col: int, piece):
        if self.board[row][col] is None:
            self.board[row][col] = piece
            return True
        else:
            print("Cell already occupied. Try again.")
            return False
    def check_winner(self, piece):
        # Check rows
        for row in self.board:
            if all(cell == piece for cell in row):
                return True

        # Check columns
        for col in range(self.size):
            if all(self.board[row][col] == piece for row in range(self.size)):
                return True

        # Check diagonals
        if all(self.board[i][i] == piece for i in range(self.size)):
            return True
        if all(self.board[i][self.size - 1 - i] == piece for i in range(self.size)):
            return True

        return False
    def get_free_cells(self):
        free_cells = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] is None:
                    free_cells.append((row, col))
        return free_cells

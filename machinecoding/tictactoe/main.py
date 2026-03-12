from TicTacToe import TicTacToe

def main():
    size = int(input("Enter the size of the board: "))
    game = TicTacToe(size)
    game.startGame()

if __name__ == "__main__":
    main()
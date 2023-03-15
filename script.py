# This is to import the library
import random

# This creates a empty board that uses strings
board = []

# This is to loop through the range of grid system that is 5*5
for i in range(5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))


print("Let's play Battleship!")
print_board(board)


def random_row(board):
    return random.randint(0, len(board) - 1)


def random_col(board):
    return random.randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

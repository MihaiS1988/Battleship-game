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


# This will define the random row from board
def random_row(board):
    return random.randint(0, len(board) - 1)


# This will define the random column from board
def random_col(board):
    return random.randint(0, len(board[0]) - 1)


# This is used to call the elements
ship_row = random_row(board)
ship_col = random_col(board)

# This for loop is uses to ask the the user to select the column and row
for turn in range(4):
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0
                                                or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif (board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if (turn == 3):
            print("Game Over")

print_board(board)
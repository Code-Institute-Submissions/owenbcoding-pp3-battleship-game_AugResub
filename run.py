from random import randint

board = []

for x in range(0, 5):
    board.append(["0"] * 5)


def print_board(board):
    for row in board:
        print(board)


print("let's play Battleship!")
print_board(board)


def random_row(board):
    return randint(0, len(board)-1)


def random_col(board):
    return randint(0, len(board)-1)


ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

for turn in range(4):
    print("Turn"), turn + 1

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

print(ship_row)
print(ship_col)

if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
else:
    if guess_row > range(5) or guess_col > range(5):
        print("Oops, thanks not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
        print("You Guessed that one already.")
    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"
    print_board(board)

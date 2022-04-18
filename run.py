# To - do
# The ability for the user to set the grid size

from random import randint

board = []

for i in range(0, 5):
    board.append(['o'] * 5)


def print_board(board):
    for row in board:
        print " ".join(row)


def rand_row(board_in):
    return randint(0, len(board_in) - 1)


def random_col(board_in):
    return randint(0, len(board_in) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

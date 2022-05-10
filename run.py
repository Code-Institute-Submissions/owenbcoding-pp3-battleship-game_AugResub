from random import randint

board = []

board_row = 5

turn_number = 1


for x in range(0, 5):
    board.append(["0"] * 5)


def print_board(board):
    # Header print - turn into a simple for loop
    print("    A B C D E")

    # Body Print
    for index_row, row in enumerate(board):
        row_render = "%s |" % index_row

        for column in row:
            row_render = row_render + " " + column

        print(row_render)


print("let's play Battleships!")
print("Player VS computer!")
print_board(board)


def random_row(board):
    return randint(0, len(board)-1)


def random_col(board):
    return randint(0, len(board)-1)


ship_col = random_col(board)
ship_row = random_row(board)
print(ship_row)
print(ship_col)

# for turn in range(4):
#     turn + 1

print("Pick a Number and a Letter")

# Start of the game loop - move to a proper method/function
for turn in range(4):
    print("Turn Number: %s" % turn)
    guess_col = (input("Guess Col:\n"))
    guess_row = int(input("Guess Row:\n"))
    try:
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sank my battleship!")
        else:
            if guess_row > board_row:
                # if guess_row > range(5) or guess_col > range(5):
                print("Oops, thanks not even in the ocean.")
            elif board[int(guess_col)][int(guess_row)] == 'X':

                print("You Guessed that one already.")
            else:
                print("You missed my battleship!")
                board[int(guess_col)][int(guess_row)] = "X"
            print_board(board)
            if turn == 3:
                print("Game Over")
    except ValueError:
        print("Ship Row: %s | Ship Column: %s" % (ship_row, ship_col))


def main():

    if __name__ == '__main__':
        main()

# To - do
# The ability for the user to set the grid size
# Warn the user if their guess is off-grid
# (shoot_bullet function) player grid of index 5, 5 computer grid of 5, 5 has an 0 but player does not then it is a hit
# get a row of letters and numbers on the left side and top of the grid

import random
import time

grid = [
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
]

num_of_ships = 2

AMMO_USER = 35

ships_sunk = 0

game_over = False

num_of_ships_sunk = 0

ship_positions = []

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# size = int(input("How Big Should the grid size be? "))

print("-----Welcome to Battleships Game-----")
print("You have 35 Torpedos to take down 2 ships, let the battle begin!")


def print_grid(grid=None, for_player='USER'):
    global alphabet

    debug_mode = True

    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")
    return True


def shipPosition():
    for ship in range(0, num_of_ships):
        ship_size = random.randint(3, 5)
        direction = random.randint(1, 4)
        rowstart = random.randint(0, len(grid))
        colstart = random.randint(0, len(grid))
        for i in range(0, ship_size):
            if rowstart + 1 > len(grid) or rowstart - 1 < 0 or colstart + 1 > len(grid) or colstart - 1 < 0:
                grid[rowstart][colstart] = "."
                rowstart = random.randint(0, len(grid))
                colstart = random.randint(0, len(grid))
            if direction == 1:
                if not grid[rowstart - 1][colstart] == "0":
                    grid[rowstart - 1][colstart] = "0"
                    rowstart = rowstart - 1
            if direction == 2:
                if not grid[rowstart][colstart + 1] == "0":
                    grid[rowstart][colstart + 1] = "0"
                    colstart = colstart + 1
            if direction == 3:
                if not grid[rowstart + 1][colstart] == "0":
                    grid[rowstart + 1][colstart] = "0"
                    rowstart = rowstart + 1
            if direction == 4:
                if not grid[rowstart][colstart - 1] == "0":
                    [rowstart][colstart - 1] = "0"
                    colstart = colstart - 1
            grid[rowstart][colstart] = "0"


shipPosition()


def main():
    """Main entry point of application that runs the game loop"""
    # global GAME_OVER

    print_grid(grid)
    print("Number of ships remaining: " +
          str(num_of_ships - num_of_ships_sunk))
    print("Number of bullets left: " + str(AMMO_USER))

    # while game_over is False:
    #     print_grid()
    #     print("Number of ships remaining: " + str(ships - ships_sunk))
    # decide_first_turn()  # random int here 0, 1

    # while True:
    #     AMMO_USER > 0 and initiate_attack('USER', to='COMPUTER')
    #     AMMO_COMPUTER > 0 and initiate_attack('COMPUTER', to='USER')
    #     decide_winner()

    # while GAME_OVER is False:
    #     print_grid()
    #     print("Number of ships remaining: " +
    #           str(num_of_ships - num_of_ships_sunk))
    #     print("Number of bullets left: " + str(bullets_left))
    #     shoot_bullet()
    #     print("----------------------------")
    #     print("")
    #     check_for_GAME_OVER()


if __name__ == '__main__':
    main()

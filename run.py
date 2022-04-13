# To - do
# The ability for the user to set the grid size
# Warn the user if their guess is off-grid
# (shoot_bullet function) player grid of index 5, 5 computer grid of 5, 5 has an 0 but player does not then it is a hit
# get a row of letters and numbers on the left side and top of the grid
#

import random
import time

ships = 2

ammo = 20
AMMO_USER = 20
AMMO_COMPUTER = 20

ships_sunk = 0

ship_positions = [[]]

size = int(input("How Big Should the grid size be? "))

print("-----Welcome to Battleship Game-----")
print("You have 50 bullets to take down 5 ships, may the battle begin!")


def generate_grid():
    grid = []
    for i in range(0, size):
        grid.append([])
        for j in range(0, size):
            random_number = random.randint(0, size)
            if j == random_number:
                grid[i].append("X")
            else:
                grid[i].append("*")
    return grid


def checkForHit(row, col):
    if grid[row][col] == "0":
        return True
    return False


def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """Will check the row or column to see if it is safe to place a ship there"""
    ship_positions = []

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid


computer_grid = generate_grid()


def shipPosition():
    for ship in range(0, ships):
        ship_size = random.randint(3, 5)
        direction = random.randint(1, 4)
        rowstart = random.randint(0, len(computer_grid))
        colstart = random.randint(0, len(computer_grid))
        for i in range(0, ship_size):
            if rowstart + 1 > len(computer_grid) or rowstart - 1 < 0 or colstart + 1 > len(computer_grid) or colstart - 1 < 0:
                computer_grid[rowstart][colstart] = "."
                rowstart = random.randint(0, len(computer_grid))
                colstart = random.randint(0, len(computer_grid))
            if direction == 1:
                if not computer_grid[rowstart - 1][colstart] == "0":
                    computer_grid[rowstart - 1][colstart] = "0"
                    rowstart = rowstart - 1
            if direction == 2:
                if not computer_grid[rowstart][colstart + 1] == "0":
                    computer_grid[rowstart][colstart + 1] = "0"
                    colstart = colstart + 1
            if direction == 3:
                if not computer_grid[rowstart + 1][colstart] == "0":
                    computer_grid[rowstart + 1][colstart] = "0"
                    rowstart = rowstart + 1
            if direction == 4:
                if not computer_grid[rowstart][colstart - 1] == "0":
                    computer_grid[rowstart][colstart - 1] = "0"
                    colstart = colstart - 1
        computer_grid[rowstart][colstart] = "0"


# player_grid = generate_grid()
# shipPosition()

# for row in range(0, size):
#     print(*(f"{computer_grid[row][col]}\t" for col in range(0, size)))
# print("player grid below")
# for row in range(0, size):
#     print(*(f"{player_grid[row][col]}\t" for col in range(0, size)))


def print_grid(grid=None, for_player='USER'):
    if grid is None:
        return False
    print(f"Displaying Grid for {for_player}")
    for i in range(0, size):
        for j in range(0, 1):
            if for_player == "COMPUTER":
                print("* " * size)
            else:
                print(" ".join(grid[i]))
    return True


def main():
    """Main entry point of application that runs the game loop"""
    global GAME_OVER

    grid = generate_grid()
    print_grid(grid)
    print_grid(grid, for_player="COMPUTER")

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

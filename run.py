import random
import time

ships = 5

ammo = 20

ships_sunk = 0

grid = []

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

size = int(input("How Big Should the grid size be? "))

def generateGrid():
    grid = []
    for i in range(0,size):
        grid.append([])
        for j in range(0,size):
            grid[i].append(".")
    return grid

def checkForHit(row, col):
    if grid[row][col] == "0":
        return True
    return False

computer_grid = generateGrid()

def shipPosition():
    for ship in range(0,ships):
        ship_size = random.randint(1, 4)
        direction = random.randint(1, 4)
        rowstart = random.randint(0, len(computer_grid))
        colstart = random.randint(0, len(computer_grid))
        for i in range(0,ship_size):
            if rowstart +1 > len(computer_grid) or rowstart -1 < 0 or colstart +1 > len(computer_grid) or colstart -1 < 0:
                computer_grid[rowstart][colstart] = "."
                rowstart = random.randint(0, len(computer_grid))
                colstart = random.randint(0, len(computer_grid))
            if direction == 1:
                if not computer_grid[rowstart -1][colstart] == "0":
                    computer_grid[rowstart -1][colstart] = "0"
                    rowstart = rowstart -1
            if direction == 2:
                if not computer_grid[rowstart][colstart +1] == "0":
                    computer_grid[rowstart][colstart +1] = "0"
                    colstart = colstart +1
            if direction == 3:
                if not computer_grid[rowstart +1][colstart] == "0":
                    computer_grid[rowstart +1][colstart] = "0"
                    rowstart = rowstart +1
            if direction == 4: 
                if not computer_grid[rowstart][colstart -1] == "0":
                    computer_grid[rowstart][colstart -1] = "0"
                    colstart = colstart -1
        computer_grid[rowstart][colstart] = "0"
player_grid = generateGrid()

shipPosition()

for row in range(0, size):
    print(*(f"{player_grid[row][col]}\t" for col in range(0, size)))
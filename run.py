import random
import time

ships = 2

ammo = 10

ships_sunk = 0

size = int(input("How Big Should the grid size be? "))

def generateGrid():
    grid = []
    for i in range(0,size):
        grid.append([])
        for j in range(0,size):
            grid[i].append(".")
    return grid

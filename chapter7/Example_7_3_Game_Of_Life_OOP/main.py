# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math
from random import random

import pygame
from cell import Cell

w = 8
columns, rows = None, None
board = None


def setup():
    global columns, rows, board
    screen = pygame.display.set_mode((640, 360))
    width, height = screen.size
    columns = int(width // w)
    rows = int(height // w)
    print(width, height, columns, rows)
    board = create2DArray(columns, rows)
    for i in range(1, columns - 1):
        for j in range(1, rows - 1):
            board[i][j] = Cell(math.floor(random() * 2), i * w, j * w, w)


def draw():
    global columns, rows, board

    # Looping but skipping the edge cells
    for x in range(1, columns - 1):
        for y in range(1, rows - 1):
            neighborSum = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # Use the previous state when counting neighbors
                    neighborSum += board[x + i][y + j].previous
            neighborSum -= board[x][y].previous

            # Set the cell's new state based on the neighbor count
            if board[x][y].state == 1 and neighborSum < 2:
                board[x][y].state = 0
            elif board[x][y].state == 1 and neighborSum > 3:
                board[x][y].state = 0
            elif board[x][y].state == 0 and neighborSum == 3:
                board[x][y].state = 1
            # else do nothing

    for x in range(columns):
        for y in range(rows):
            # evaluates to 255 when state is 0 and 0 when state is 1
            board[x][y].show()

            # save the previous state before the next generation!
            board[x][y].previous = board[x][y].state

    # Click to restart
    if pygame.mouse.get_just_pressed()[0]:
        for x in range(1, columns - 1):
            for y in range(1, rows - 1):
                board[x][y] = Cell(math.floor(random() * 2), x * w, y * w, w)


def create2DArray(columns, rows):
    return [[Cell(0, i * w, j * w, w) for j in range(rows)] for i in range(columns)]


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    setup()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()
        pygame.display.update()
        clock.tick(60)

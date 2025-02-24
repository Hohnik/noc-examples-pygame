# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math
from random import random

import pygame

w = 8
columns, rows = None, None
board = None


def setup():
    global columns, rows, board
    screen = pygame.display.set_mode((640, 360))
    width, height = screen.size
    columns = int(width // w)
    rows = int(height // w)
    board = create2DArray(columns, rows)
    for i in range(1, columns - 1):
        for j in range(1, rows - 1):
            board[i][j] = math.floor(random() * 2)


def draw():
    global columns, rows, board
    screen = pygame.display.get_surface()

    # The next board
    next = create2DArray(columns, rows)

    # Looping but skipping the edge cells
    for i in range(1, columns - 1):
        for j in range(1, rows - 1):
            # Add up all the neighbor states to
            # calculate the number of live neighbors.
            neighborSum = 0
            for m in range(-1, 2):
                for n in range(-1, 2):
                    neighborSum += board[i + m][j + n]

            # Correct by subtracting the cell state itself.
            neighborSum -= board[i][j]

            # The rules of life!
            if board[i][j] == 1 and neighborSum < 2:
                next[i][j] = 0
            elif board[i][j] == 1 and neighborSum > 3:
                next[i][j] = 0
            elif board[i][j] == 0 and neighborSum == 3:
                next[i][j] = 1
            else:
                next[i][j] = board[i][j]

    for i in range(columns):
        for j in range(rows):
            # evaluates to 255 when state is 0 and 0 when state is 1
            c = 255 - board[i][j] * 255
            pygame.draw.rect(screen, (c, c, c), (i * w, j * w, w, w))

    board = next

    # Click to restart
    if pygame.mouse.get_just_pressed()[0]:
        board = create2DArray(columns, rows)
        for i in range(1, columns - 1):
            for j in range(1, rows - 1):
                board[i][j] = math.floor(random() * 2)


def create2DArray(columns, rows):
    return [[0 for _ in range(rows)] for _ in range(columns)]


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

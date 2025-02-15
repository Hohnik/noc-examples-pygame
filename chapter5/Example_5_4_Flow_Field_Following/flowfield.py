# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math
from random import randint

import pygame
from noise import pnoise2


def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def constrain(value, min_val, max_val):
    return max(min_val, min(value, max_val))


class FlowField:
    def __init__(self, screen, r):
        self.screen = screen
        self.resolution = r

        # Determine the number of columns and rows.
        self.cols = screen.get_width() // self.resolution
        self.rows = screen.get_height() // self.resolution

        # A flow field is a two-dimensional array of vectors. The example includes as separate function to create that array
        self.field = [[None for _ in range(self.rows)] for _ in range(self.cols)]
        self.init()

    # The init() function fills the 2D array with vectors
    def init(self):
        # Reseed noise for a new flow field each time
        seed = randint(0, 10000)
        xoff = 0 + seed
        for i in range(self.cols):
            yoff = 0 + seed
            for j in range(self.rows):
                # In self example, use Perlin noise to create the vectors.
                angle = map_value(pnoise2(xoff, yoff), 0, 1, 0, 360)
                vec = pygame.Vector2()
                vec.from_polar((1, angle))
                self.field[i][j] = vec
                yoff += 0.1

            xoff += 0.1

    # Draw every vector
    def show(self):
        width = self.screen.get_width()
        height = self.screen.get_height()
        for i in range(self.cols):
            for j in range(self.rows):
                w = width / self.cols
                h = height / self.rows
                v = self.field[i][j].copy()
                v.scale_to_length(w * 0.5)
                x = i * w + w / 2
                y = j * h + h / 2
                pygame.draw.line(self.screen, "black", (x, y), (x + v.x, y + v.y))

    # A function to return a pygame.Vector2 based on a position
    def lookup(self, position):
        column = constrain(math.floor(position.x / self.resolution), 0, self.cols - 1)
        row = constrain(math.floor(position.y / self.resolution), 0, self.rows - 1)
        return self.field[column][row].copy()

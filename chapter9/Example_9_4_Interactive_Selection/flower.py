# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math

import pygame
from rectangle import Rectangle
from utils import map_value

# Interactive Selection
# http://www.genarts.com/karl/papers/siggraph91.html

# The class for a "face", contains DNA sequence, fitness value, position on screen

# Fitness Function f(t) = t (where t is "time" mouse rolls over face)
# Create a new flower


class Flower:
    def __init__(self, dna, x, y):
        self.screen = pygame.display.get_surface()
        assert self.screen, "Initialize pygame display before creating Flower"

        self.rolloverOn = False  # Are we rolling over this flower?
        self.dna = dna  # Flower's DNA
        self.x = x
        self.y = y
        self.w = 70  # Size of square enclosing flower
        self.h = 140  # Size of square enclosing flower
        self.fitness = 1  # How good is this flower?
        self.boundingBox = Rectangle(self.x, self.y, self.w, self.h)

    # Display the flower
    def show(self):
        genes = self.dna.genes
        # TODO: is the color passing correct?
        c = (genes[0], genes[1], genes[2])  # petal color (no alpha)
        size = map_value(genes[4], 0, 1, 4, 24)  # petal size
        count = math.floor(map_value(genes[5], 0, 1, 2, 26))  # petal count
        centerColor = (genes[6], genes[7], genes[8])  # center color
        centerSize = map_value(genes[9], 0, 1, 24, 48)  # center size
        stemColor = (genes[10], genes[11], genes[12])  # stem color
        stemLength = map_value(genes[13], 0, 1, 50, 100)  # stem length

        assert self.screen

        # Draw bounding box
        if self.rolloverOn:
            pygame.draw.rect(
                self.screen, (190, 190, 190), (self.x, self.y, self.w, self.h)
            )

        pygame.draw.rect(
            self.screen, (190, 190, 190), (self.x, self.y, self.w, self.h), 1
        )

        # Draw the stem
        pygame.draw.line(
            self.screen,
            stemColor,
            (self.x + 0.5 * self.w, self.y + self.h),
            (self.x + 0.5 * self.w, self.y + self.h - stemLength),
        )

        # Draw petal

        # Draw the center

        # Display fitness value

    def rollover(self, mx, my):
        if self.boundingBox.contains(mx, my):
            self.rolloverOn = True
            self.fitness += 0.25
        else:
            self.rolloverOn = False

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math

import pygame
from rectangle import Rectangle
from utils import Text, map_value

# Interactive Selection
# http://www.genarts.com/karl/papers/siggraph91.html

# The class for a "face", contains DNA sequence, fitness value, position on screen

# Fitness Function f(t) = t (where t is "time" mouse rolls over face)
# Create a new flower


class Flower:
    def __init__(self, dna, x, y):
        self.screen = pygame.display.get_surface()
        assert self.screen, "Initialize pygame display before creating Flower"
        self.font = pygame.font.SysFont("courier", 12)

        self.rolloverOn = False  # Are we rolling over this flower?
        self.dna = dna  # Flower's DNA
        self.x = x
        self.y = y
        self.w = 70  # Size of square enclosing flower
        self.h = 140  # Size of square enclosing flower
        self.fitness = 1  # How good is this flower?
        self.boundingBox = Rectangle(self.x, self.y, self.w, self.h)

        self.text = Text(x + 0.5 * self.w, y + self.h + 10, self.font, anchor="center")

    # Display the flower
    def show(self):
        assert self.screen

        genes = self.dna.genes
        # TODO: is the color passing correct?
        c = (genes[0] * 255, genes[1] * 255, genes[2] * 255)  # petal color
        alpha = map_value(genes[3], 0, 1, 50, 255)  # petal opacity
        size = map_value(genes[4], 0, 1, 4, 24)  # petal size
        count = math.floor(map_value(genes[5], 0, 1, 2, 26))  # petal count
        centerColor = (genes[6] * 255, genes[7] * 255, genes[8] * 255)  # center color
        centerSize = map_value(genes[9], 0, 1, 24, 48)  # center size
        stemColor = (genes[10] * 255, genes[11] * 255, genes[12] * 255)  # stem color
        stemLength = map_value(genes[13], 0, 1, 50, 100)  # stem length

        assert self.screen

        # Draw bounding box
        if self.rolloverOn:
            pygame.draw.rect(
                self.screen, (190, 190, 190), (self.x, self.y, self.w, self.h)
            )
        pygame.draw.rect(self.screen, "black", (self.x, self.y, self.w, self.h), 1)

        # Draw the stem
        stemBottom = (self.x + 0.5 * self.w, self.y + self.h)
        stemTop = (self.x + 0.5 * self.w, self.y + self.h - stemLength)
        pygame.draw.line(self.screen, stemColor, stemBottom, stemTop)

        # Draw petal
        petals = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        stemTopX, stemTopY = stemTop
        for i in range(count):
            angle = map_value(i, 0, count, 0, math.pi * 2)
            x = size * math.cos(angle)
            y = size * math.sin(angle)
            pygame.draw.circle(
                petals, (*c, alpha), (stemTopX + x, stemTopY + y), 0.5 * size
            )
        self.screen.blit(petals, (0, 0))

        # Draw the center
        pygame.draw.circle(self.screen, centerColor, stemTop, centerSize / 2)

        # Display fitness value
        self.text.set_text(f"{math.floor(self.fitness)}")
        self.text.draw(self.screen)

    def rollover(self, mx, my):
        if self.boundingBox.contains(mx, my):
            self.rolloverOn = True
            self.fitness += 0.25
        else:
            self.rolloverOn = False

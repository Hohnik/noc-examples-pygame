# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Evolution EcoSystem

from random import random

import noise
import pygame
from utils import map_value

# Creature class

# Create a "bloop" creature


class Bloop:
    def __init__(self, position, dna):
        self.screen = pygame.display.get_surface()
        assert self.screen, "No pygame display surface found."

        self.position = position  # Location
        self.health = 200  # Life timer
        self.xoff = random() * 1000  # For perlin noise
        self.yoff = random() * 1000
        self.dna = dna  # DNA

        # DNA will determin size and maxspeed
        # The bigger the bloop the slower it is
        self.maxspeed = map_value(
            self.dna.genes[0], 0, 1, 15, 0
        )  # WARNING: is this working with 15, 0 ?
        self.r = map_value(self.dna.genes[0], 0, 1, 0, 25)

    def run(self):
        self.update()
        self.borders()
        self.show()

    # A bloop can find food and eat it
    def eat(self, food):
        # Check all the food vectors
        positions = food.foodPositions

        for i in range(len(positions) - 1, -1, -1):
            # How far away is the bloop?
            distance = pygame.Vector2(*self.position).distance_to(positions[i])

            # If the food is nearby
            if distance < self.r * 2:
                # Increase health and remove the food!
                self.health += 100
                positions.pop(i)

    # At any moment there is a teeny, tiny chance a bloop will reproduce
    def reproduce(self):
        # Single parent reproduction
        if random() < 0.0005:
            # Child is exact copy of single parent
            childDNA = self.dna.copy()

            # Child DNA can mutate
            childDNA.mutate(0.01)

            return Bloop(self.position.copy(), childDNA)

    # Method to update position
    def update(self):
        # Simple movement based on perlin noise
        vx = map_value(
            noise.pnoise1(self.xoff) * 0.5 + 0.5, 0, 1, -self.maxspeed, self.maxspeed
        )
        vy = map_value(
            noise.pnoise1(self.yoff) * 0.5 + 0.5, 0, 1, -self.maxspeed, self.maxspeed
        )
        velocity = pygame.Vector2(vx, vy)
        self.xoff += 0.01
        self.yoff += 0.01

        self.position += velocity

        # Death is always looming
        self.health -= 0.2

    # Wraparound
    def borders(self):
        assert self.screen
        if self.position.x < -self.r:
            self.position.x = self.screen.get_width() + self.r
        if self.position.y < self.r:
            self.position.y = self.screen.get_height() + self.r
        if self.position.x > self.screen.get_width() + self.r:
            self.position.x = -self.r
        if self.position.y > self.screen.get_height() + self.r:
            self.position.y = -self.r

    # Method to display
    def show(self):
        assert self.screen
        d = int(self.r * 2) + 2
        circle = pygame.Surface((d, d), pygame.SRCALPHA)
        color = (0, 0, 0, int(pygame.math.clamp(self.health, 0, 255)))
        pygame.draw.aacircle(circle, (color), (d / 2, d / 2), self.r)
        self.screen.blit(circle, (self.position.x - d / 2, self.position.y - d / 2))

    # Death
    def dead(self):
        return self.health < 0.0

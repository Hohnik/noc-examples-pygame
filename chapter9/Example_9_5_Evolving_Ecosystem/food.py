# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Evolution EcoSystem

from random import random

import pygame

# A collection of food in the world


class Food:
    def __init__(self, num):
        self.screen = pygame.display.get_surface()
        assert self.screen, "No pygame display surface found."

        # Start with some food
        self.foodPositions = []
        for _ in range(num):
            self.foodPositions.append(
                pygame.Vector2(
                    random() * self.screen.get_width(),
                    random() * self.screen.get_height(),
                )
            )

    # Add some food at a location
    def add(self, position):
        self.foodPositions.append(position.copy())

    # Display the food
    def run(self):
        assert self.screen
        for position in self.foodPositions:
            rect = (position.x - 4, position.y - 4, 8, 8)
            pygame.draw.rect(self.screen, (200, 200, 200), rect)
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

        # There's a small chance food will appear randomly
        if random() < 0.001:
            self.foodPositions.append(
                pygame.Vector2(
                    random() * self.screen.get_width(),
                    random() * self.screen.get_height(),
                )
            )

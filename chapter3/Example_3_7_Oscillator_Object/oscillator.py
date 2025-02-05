# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math
from random import random

import pygame


class Oscillator:
    def __init__(self, screen):
        self.screen = screen
        self.angle = pygame.Vector2()
        self.angleVelocity = pygame.Vector2(
            random() * 0.10 - 0.05, random() * 0.10 - 0.05
        )
        self.amplitude = pygame.Vector2(
            random() * (screen.get_width() - 20) / 2 + 20,
            random() * (screen.get_height() - 20) / 2 + 20,
        )

    def update(self):
        self.angle += self.angleVelocity

    def show(self):
        x = math.sin(self.angle.x) * self.amplitude.x
        y = math.sin(self.angle.y) * self.amplitude.y

        center = pygame.Vector2(
            self.screen.get_width() / 2, self.screen.get_height() / 2
        )
        pygame.draw.line(self.screen, "black", center, (x + center.x, y + center.y), 2)
        pygame.draw.aacircle(self.screen, "gray50", (x + center.x, y + center.y), 16)
        pygame.draw.aacircle(self.screen, "black", (x + center.x, y + center.y), 16, 1)

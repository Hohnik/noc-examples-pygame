# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
import random

import pygame


class Mover:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.position = pygame.Vector2(
            random.random() * screen.get_width(), random.random() * screen.get_height()
        )
        self.velocity = pygame.Vector2(random.random() * 4 - 2, random.random() * 4 - 2)

    def update(self):
        self.position += self.velocity

    def show(self):
        pygame.draw.circle(self.screen, "gray50", self.position, 24)
        pygame.draw.circle(self.screen, "black", self.position, 24, 2)

    def checkEdges(self):
        if self.position.x > self.screen.get_width():
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = self.screen.get_width()

        if self.position.y > self.screen.get_height():
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = self.screen.get_height()

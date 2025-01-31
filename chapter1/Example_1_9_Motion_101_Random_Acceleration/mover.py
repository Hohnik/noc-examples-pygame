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
        self.velocity = pygame.Vector2()
        self.acceleration = pygame.Vector2()
        self.topSpeed = 5

    def update(self):
        # The random2D() function returns a unit vector pointing in a random direction.
        self.acceleration = pygame.Vector2(
            random.random() - 0.5, random.random() - 0.5
        ).normalize()
        self.acceleration *= random.random() * 2

        self.velocity += self.acceleration
        self.velocity = self.velocity.clamp_magnitude(self.topSpeed)
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

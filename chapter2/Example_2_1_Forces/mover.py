# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame


class Mover:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.mass = 1
        self.position = pygame.Vector2(screen.get_width() / 2, 30)
        self.velocity = pygame.Vector2()
        self.acceleration = pygame.Vector2()

    def applyForce(self, force):
        f = force / self.mass
        self.acceleration += f

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

    def show(self):
        pygame.draw.circle(self.screen, "gray50", self.position, 24)
        pygame.draw.circle(self.screen, "black", self.position, 24, 2)

    def checkEdges(self):
        if self.position.x > self.screen.get_width():
            self.position.x = self.screen.get_width()
            self.velocity.x *= -1
        elif self.position.x < 0:
            self.velocity.x *= -1
            self.position.x = 0

        if self.position.y > self.screen.get_height():
            self.velocity.y *= -1
            self.position.y = self.screen.get_height()

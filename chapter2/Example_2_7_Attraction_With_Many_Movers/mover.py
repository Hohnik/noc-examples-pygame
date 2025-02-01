# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame


class Mover:
    def __init__(self, screen: pygame.Surface, x, y, mass):
        self.screen = screen
        self.mass = mass
        self.radius = mass * 8
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(1, 0)
        self.acceleration = pygame.Vector2()

    # Newton's 2nd law: F = M * A
    # or A = F / M
    def applyForce(self, force):
        f = force / self.mass
        self.acceleration += f

    def update(self):
        # Velocity changes according to acceleration
        self.velocity += self.acceleration
        # position changes by velocity
        self.position += self.velocity
        # We must clear acceleration each frame
        self.acceleration *= 0

    def show(self):
        pygame.draw.aacircle(self.screen, "gray50", self.position, self.radius)
        pygame.draw.aacircle(self.screen, "black", self.position, self.radius, 2)

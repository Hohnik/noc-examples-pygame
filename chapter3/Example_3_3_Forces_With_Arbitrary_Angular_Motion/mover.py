# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from random import random

import pygame


class Mover:
    def __init__(self, screen: pygame.Surface, x, y, mass):
        self.screen = screen
        self.mass = mass
        self.radius = mass * 8
        self.position = pygame.Vector2(x, y)
        self.angle = 0
        self.angleVelocity = 0
        self.angleAcceleration = 0
        self.velocity = pygame.Vector2(random() * 2 - 1, random() * 2 - 1)
        self.acceleration = pygame.Vector2()

    def applyForce(self, force):
        f = force / self.mass
        self.acceleration += f

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.angleAcceleration = self.acceleration.x / 10.0
        self.angleVelocity += self.angleAcceleration
        self.angleVelocity = pygame.math.clamp(self.angleVelocity, -0.1, 0.1)
        self.angle += self.angleVelocity
        self.acceleration *= 0

    def show(self):
        pygame.draw.aacircle(self.screen, "gray50", (self.position), self.radius)
        pygame.draw.aacircle(self.screen, "black", (self.position), self.radius, 1)

        direction = pygame.Vector2(1, 0)
        direction.scale_to_length(self.radius)

        center = self.position
        head = self.position + direction.rotate_rad(self.angle)
        pygame.draw.aaline(self.screen, "black", (center), (head))

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math

import pygame


class Body:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2()
        self.acceleration = pygame.Vector2()
        self.mass = 8
        self.r = math.sqrt(self.mass) * 2

    def attract(self, body):
        force = self.position - body.position
        d = pygame.math.clamp(force.magnitude(), 5, 25)
        G = 1
        strength = (G * (self.mass * body.mass)) / d**2
        force.scale_to_length(strength)
        body.applyForce(force)

    def applyForce(self, force):
        f = force / self.mass
        self.acceleration += f

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration.xy = 0, 0

    def show(self):
        pygame.draw.aacircle(self.screen, "gray70", self.position, self.r * 3)
        pygame.draw.aacircle(self.screen, "black", self.position, self.r * 3, 2)

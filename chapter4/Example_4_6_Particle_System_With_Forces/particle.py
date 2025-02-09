# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Simple Particle System

# A simple Particle class

from random import random

import pygame


class Particle:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.position = pygame.Vector2(x, y)
        self.acceleration = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(random() * 2 - 1, random() - 1)
        self.lifespan = 255.0
        self.mass = 1  # Let's do something better here!
        self.r = 4

    def run(self):
        self.update()
        self.show()

    def applyForce(self, force):
        f = force.copy()
        f /= self.mass
        self.acceleration += force

    # Method to update position
    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0
        self.lifespan -= 2.0

    # Method to display
    def show(self):
        rect = pygame.Surface((self.r * 2, self.r * 2), pygame.SRCALPHA)
        rect_center = pygame.Vector2(self.r, self.r)
        lifespan = int(pygame.math.clamp(self.lifespan, 0, 255))
        pygame.draw.circle(rect, (0, 0, 0, lifespan), rect_center, self.r)
        self.screen.blit(rect, self.position - rect_center)

    # Is the Particle still usefull?
    def isDead(self):
        return self.lifespan < 0

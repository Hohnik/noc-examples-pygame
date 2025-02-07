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
        # For demonstration purposes the Particle has a random velocity.
        self.velocity = pygame.Vector2(random() * 2 - 1, random() * 2 - 2)
        self.acceleration = pygame.Vector2(0, 0)
        self.lifespan = 255.0
        self.r = 4

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.lifespan -= 2.0
        self.acceleration *= 0

    def show(self):
        rect = pygame.Surface((self.r * 2, self.r * 2), pygame.SRCALPHA)
        rect_center = pygame.Vector2(self.r, self.r)
        lifespan = int(pygame.math.clamp(self.lifespan, 0, 255))
        pygame.draw.circle(rect, (0, 0, 0, lifespan), rect_center, self.r)
        self.screen.blit(rect, self.position - rect_center)

    # Keeping the same physics model as with previous chapters
    def applyForce(self, force):
        self.acceleration += force

    # Is the Particle alive or dead?
    def isDead(self):
        return self.lifespan < 0

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from random import gauss

import pygame

# Simple Particle System

# A simple Particle class


class Particle:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.position = pygame.Vector2(x, y)
        vx = gauss(0, 0.3)
        vy = gauss(-1, 0.3)
        self.velocity = pygame.Vector2(vx, vy)
        self.acceleration = pygame.Vector2(0, 0)
        self.lifespan = 100.0

    def run(self, img):
        self.update()
        self.show(img)

    # Method to apply a force vector to the Particle object
    # Note we are ignoring "mass" here
    def applyForce(self, force):
        self.acceleration += force

    # Method to update position
    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.lifespan -= 2.0
        self.acceleration *= 0  # clear Acceleration

    # Method to draw
    def show(self, img):
        img.set_alpha(self.lifespan)
        img_rect = img.get_rect(center=self.position)
        self.screen.blit(img, img_rect)

        # Draw a circle instead
        # pygame.draw.circle(self.screen, (self.lifespan, self.lifespan, self.lifespan), self.position, 4)

    # Is the Particle still usefull?
    def isDead(self):
        return self.lifespan < 0

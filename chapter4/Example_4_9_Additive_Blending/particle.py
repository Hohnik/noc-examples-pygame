# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from random import gauss

import pygame

# Simple Particle System

# A simple Particle class


class Particle:
    def __init__(self, screen, x, y, img):
        self.screen = screen
        self.img = img
        self.r = 15
        self.position = pygame.Vector2(x, y)
        vx = gauss(0, 0.3)
        vy = gauss(-1, 0.3)
        self.velocity = pygame.Vector2(vx, vy)
        self.acceleration = pygame.Vector2(0, 0)
        self.lifespan = 100.0

    def run(self):
        self.update()
        self.show()

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
    def show(self):
        lifespan = int(self.lifespan) if self.lifespan > 0 else 0

        surf = pygame.Surface((self.r * 2, self.r * 2))
        pygame.draw.circle(
            surf, (lifespan * 2.5, lifespan, lifespan * 2.5), (self.r, self.r), self.r
        )
        self.img.set_colorkey((0, 0, 0))
        self.screen.blit(
            surf,
            (self.position.x - self.r, self.position.y - self.r),
            special_flags=pygame.BLEND_ADD,
        )

        # self.img.set_colorkey((0,0,0))
        # self.screen.blit(self.img,(self.position.x - self.r, self.position.y - self.r), special_flags=pygame.BLEND_ADD)

        pygame.draw.circle(
            self.screen,
            (lifespan * 2.5, lifespan * 2.5, lifespan * 2.5),
            self.position,
            self.r * 0.7,
        )

    # Is the Particle still usefull?
    def isDead(self):
        return self.lifespan < 0

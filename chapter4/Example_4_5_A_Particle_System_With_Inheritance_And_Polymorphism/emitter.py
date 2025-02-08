# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from random import random

import pygame
from confetti import Confetti
from particle import Particle


class Emitter:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.origin = pygame.Vector2(x, y)
        self.particles = []

    def addParticle(self):
        r = random()
        if r < 0.5:
            self.particles.append(Particle(self.screen, self.origin.x, self.origin.y))
        else:
            self.particles.append(Confetti(self.screen, self.origin.x, self.origin.y))

    def run(self):
        for i in range(len(self.particles) - 1, -1, -1):
            p = self.particles[i]
            p.run()
            if p.isDead():
                self.particles.pop(i)

        # Alternatively
        # for particle in self.particles:
        #     particle.run()
        # self.particles = list(filter(lambda particle: not particle.isDead(), self.particles))

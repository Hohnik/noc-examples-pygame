# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from particle import Particle


# The Emitter manages all the particles.
class Emitter:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.origin = pygame.Vector2(x, y)
        self.particles = []

    def addParticle(self):
        self.particles.append(Particle(self.screen, self.origin.x, self.origin.y))

    def applyForce(self, force):
        # Applying a force as a pygame.Vector2
        for particle in self.particles:
            particle.applyForce(force)

    def applyRepeller(self, repeller):
        # Calculating a force for each Particle based on a Repeller
        for particle in self.particles:
            force = repeller.repel(particle)
            particle.applyForce(force)

    def run(self):
        # Looping through backwards to delete
        for i in range(len(self.particles) - 1, -1, -1):
            self.particles[i].run()
            if self.particles[i].isDead():
                # Remove the particle
                self.particles.pop(i)

        # Alternatively
        # for particle in self.particles:
        #     particle.run()
        # self.particles = list(filter(lambda particle: not particle.isDead(), self.particles))

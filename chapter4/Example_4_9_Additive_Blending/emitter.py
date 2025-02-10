# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from particle import Particle

# Smoke Particle System

# A class to descrie a group of Particles
# An ArrayList is used to manage the list of Particles


class Emitter:
    def __init__(self, screen, x, y, img):
        self.screen = screen
        self.img = img
        self.particles = []  # Inititialize the arraylist
        self.origin = pygame.Vector2(x, y)  # Store the origin point

    def run(self):
        for particle in self.particles:
            particle.run()
        self.particles = list(
            filter(lambda particle: not particle.isDead(), self.particles)
        )

    # Method to add a force vector to all particles currently in the system
    def applyForce(self, force):
        # Enhanced loop!!!
        for particle in self.particles:
            particle.applyForce(force)

    def addParticle(self):
        self.particles.append(
            Particle(self.screen, self.origin.x, self.origin.y, self.img)
        )

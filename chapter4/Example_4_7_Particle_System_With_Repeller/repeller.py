# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame


class Repeller:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.position = pygame.Vector2(x, y)
        # How strong is the repeller?
        self.power = 150

    def show(self):
        pygame.draw.circle(self.screen, "gray50", self.position, 16)
        pygame.draw.circle(self.screen, "black", self.position, 16, 2)

    def repel(self, particle):
        # self is the same repel algorithm we used in Chapter 2: forces based on gravitational attraction.
        force = self.position - particle.position
        distance = force.magnitude()
        distance = pygame.math.clamp(distance, 5, 50)
        strength = (-1 * self.power) / (distance * distance)
        force.scale_to_length(strength)
        return force

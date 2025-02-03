# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame


class Attractor:
    def __init__(self, screen):
        self.screen = screen
        self.position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.mass = 20
        self.G = 1

    def attract(self, mover):
        # Calculate direction of force
        force = self.position - mover.position
        # Distance between objects
        distance = force.magnitude()
        # Limiting the distance to eliminate "extreme" results for very close or very far objects
        distance = pygame.math.clamp(distance, 5, 25)

        # Calculate gravitional force magnitude
        strength = (self.G * self.mass * mover.mass) / (distance * distance)
        # Get force vector --> magnitude * direction
        force.scale_to_length(strength)
        return force

    # Method to display
    def show(self):
        color = (175, 175, 175)

        pygame.draw.aacircle(self.screen, color, self.position, self.mass)
        pygame.draw.aacircle(self.screen, (0, 0, 0), self.position, self.mass, 1)

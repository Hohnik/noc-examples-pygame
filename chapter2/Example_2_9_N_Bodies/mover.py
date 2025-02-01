# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

G = 1


class Body:
    def __init__(self, screen: pygame.Surface, x, y, mass):
        self.screen = screen
        self.mass = mass
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2()
        self.acceleration = pygame.Vector2()

    def applyForce(self, force):
        f = force / self.mass
        self.acceleration += f

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

    def show(self):
        pygame.draw.aacircle(self.screen, "gray70", self.position, self.mass * 8)
        pygame.draw.aacircle(self.screen, "black", self.position, self.mass * 8, 2)

    def attract(self, other):
        # Calculate direction of force
        force = self.position - other.position
        # Distance between objects
        distance = force.magnitude()
        # Limiting the distance to eliminate "extreme" results for very close or very far objects
        distance = pygame.math.clamp(distance, 5, 25)

        # Calculate gravitational force magnitude
        strength = (G * self.mass * other.mass) / distance**2
        # Get force vector --> magnitude * direction
        force.scale_to_length(strength)
        return force

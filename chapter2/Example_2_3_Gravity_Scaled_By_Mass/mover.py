# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame


class Mover:
    def __init__(self, screen: pygame.Surface, x, y, m):
        self.screen = screen
        self.mass = m
        self.radius = m * 8
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

    def display(self):
        pygame.draw.aacircle(
            self.screen, "gray50", self.position, self.radius
        )  # Draw a antialiased circle
        pygame.draw.aacircle(self.screen, "black", self.position, self.radius, 2)

    def checkEdges(self):
        if self.position.x > self.screen.get_width() - self.radius:
            self.position.x = self.screen.get_width() - self.radius
            self.velocity.x *= -1
        elif self.position.x < self.radius:
            self.position.x = self.radius
            self.velocity.x *= -1

        if self.position.y > self.screen.get_height() - self.radius:
            self.position.y = self.screen.get_height() - self.radius
            self.velocity.y *= -1

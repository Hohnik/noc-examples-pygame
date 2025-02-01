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

    def show(self):
        pygame.draw.aacircle(self.screen, "gray50", self.position, self.radius)
        pygame.draw.aacircle(self.screen, "black", self.position, self.radius, 2)

    def contactEdge(self):
        # The mover is touching the edge when it's within one pixel
        return self.position.y > self.screen.get_height() - self.radius - 1

    def bounceEdges(self):
        # A new variable to simulate an inelastic collision
        # 10% of the velocity's x or y component is lost
        bounce = -0.9
        if self.position.x > self.screen.get_width() - self.radius:
            self.position.x = self.screen.get_width() - self.radius
            self.velocity.x *= bounce
        elif self.position.x < self.radius:
            self.position.x = self.radius
            self.velocity.x *= bounce

        if self.position.y > self.screen.get_height() - self.radius:
            self.position.y = self.screen.get_height() - self.radius
            self.velocity.y *= bounce

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math

import pygame


def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


# The "Vehicle" class
class Vehicle:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(3, 4)
        self.acceleration = pygame.Vector2(0, 0)
        self.r = 6
        self.maxspeed = 3
        self.maxforce = 0.15

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity += self.acceleration
        # Limit speed
        self.velocity.clamp_magnitude_ip(self.maxspeed)
        self.position += self.velocity
        # Reset accelerationelertion to 0 each cycle
        self.acceleration *= 0

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration += force

    def boundaries(self, offset):
        desired = None

        if self.position.x < offset:
            desired = pygame.Vector2(self.maxspeed, self.velocity.y)
        elif self.position.x > self.screen.get_width() - offset:
            desired = pygame.Vector2(-self.maxspeed, self.velocity.y)

        if self.position.y < offset:
            desired = pygame.Vector2(self.velocity.x, self.maxspeed)
        elif self.position.y > self.screen.get_height() - offset:
            desired = pygame.Vector2(self.velocity.x, -self.maxspeed)

        if desired is not None:
            desired.normalize_ip()
            desired *= self.maxspeed
            steer = desired - self.velocity
            steer.clamp_magnitude_ip(self.maxforce)
            self.applyForce(steer)

    def show(self):
        # Vehicle is a triangle pointing in the direction of velocity
        offset = self.position

        angle = math.degrees(math.atan2(self.velocity.y, self.velocity.x))

        head = pygame.Vector2(self.r * 2, 0).rotate(angle)
        back_left = pygame.Vector2(-self.r * 2, -self.r).rotate(angle)
        back_right = pygame.Vector2(-self.r * 2, self.r).rotate(angle)

        pygame.draw.polygon(
            self.screen,
            "gray50",
            [head + offset, back_left + offset, back_right + offset],
        )
        pygame.draw.polygon(
            self.screen,
            "black",
            [head + offset, back_left + offset, back_right + offset],
            2,
        )

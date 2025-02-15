# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math

import pygame


# The "Vehicle" class
class Vehicle:
    def __init__(self, screen, x, y, ms, mf):
        self.screen = screen
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2()
        self.acceleration = pygame.Vector2()
        self.r = 4
        self.maxspeed = ms
        self.maxforce = mf

    def run(self):
        self.update()
        self.borders()
        self.show()

    # Implementing Reynolds' flow field following algorithm
    # http://www.red3d.com/cwr/steer/FlowFollow.html
    def follow(self, flow):
        # What is the vector at the spot in the flow field?
        desired = flow.lookup(self.position)
        # Scale it up by maxspeed
        desired *= self.maxspeed
        # Steering is `desired - velocity`
        steer = desired - self.velocity
        steer.clamp_magnitude_ip(
            self.maxforce
        )  # Limit to maximum steering force # Limit to maximum steering force
        self.applyForce(steer)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration += force

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity += self.acceleration
        # Limit speed
        self.velocity.clamp_magnitude_ip(self.maxspeed)
        self.position += self.velocity
        # Reset accelerationelertion to 0 each cycle
        self.acceleration *= 0

    # Wraparound
    def borders(self):
        width = self.screen.get_width()
        height = self.screen.get_height()
        if self.position.x < -self.r:
            self.position.x = width + self.r
        if self.position.y < -self.r:
            self.position.y = height + self.r
        if self.position.x > width + self.r:
            self.position.x = -self.r
        if self.position.y > height + self.r:
            self.position.y = -self.r

    def show(self):
        # Draw a triangle rotated in the direction of velocity
        theta = math.degrees(math.atan2(self.velocity.y, self.velocity.x))

        head = pygame.Vector2(self.r * 2, 0).rotate(theta)
        back_left = pygame.Vector2(-self.r * 2, -self.r).rotate(theta)
        back_right = pygame.Vector2(-self.r * 2, self.r).rotate(theta)

        offset = self.position  # Translation
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

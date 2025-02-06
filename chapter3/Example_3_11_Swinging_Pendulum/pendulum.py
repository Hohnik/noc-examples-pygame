import math

import pygame

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Pendulum

# A Simple Pendulum Class


# This constructor could be improved to allow a greater variety of pendulums
class Pendulum:
    def __init__(self, screen, x, y, r):
        self.screen = screen
        # Fill all variables
        self.pivot = pygame.Vector2(x, y)
        self.bob = pygame.Vector2(100, 100)
        self.r = r
        self.angle = math.pi / 4

        self.angleVelocity = 0.0
        self.angleAcceleration = 0.0
        self.damping = 0.995
        self.ballr = 24
        self.dragging = False

    # Function to update position
    def update(self):
        # As long as we aren't dragging the pendulum, let it swing!
        if not self.dragging:
            gravity = 0.4  # Arbitrary constant
            self.angleAcceleration = (
                ((-1 * gravity) / self.r) * math.sin(self.angle)
            )  # Calculate acceleration (see: http://www.myphysicslab.com/pendulum1.html)

            self.angleVelocity += self.angleAcceleration  # Increment velocity
            self.angle += self.angleVelocity  # Increment angle

            self.angleVelocity *= self.damping  # Apply some damping

    def show(self):
        self.bob = pygame.Vector2(
            self.r * math.sin(self.angle), self.r * math.cos(self.angle)
        )  # Polar to cartesian conversion
        self.bob += (
            self.pivot
        )  # Make sure the position is relative to the pendulum's origin

        # Draw the arm
        pygame.draw.line(self.screen, "black", self.pivot, self.bob, 2)

        # Draw the ball
        pygame.draw.circle(self.screen, "gray50", self.bob, self.ballr)
        pygame.draw.circle(self.screen, "black", self.bob, self.ballr, 2)

    # The methods below are for mouse interaction

    # This checks to see if we clicked on the pendulum ball
    def clicked(self, mx, my):
        d = self.bob.distance_to((mx, my))
        if d < self.ballr:
            self.dragging = True

    # This tells us we are not longer clicking on the ball
    def stopDragging(self):
        self.angleVelocity = 0  # No velocity once you let go
        self.dragging = False

    def drag(self):
        # If we are draging the ball, we calculate the angle between the
        # pendulum origin and mouse position
        # we assign that angle to the pendulum
        if self.dragging:
            diff = self.pivot - pygame.Vector2(
                pygame.mouse.get_pos()
            )  # Difference between 2 points
            self.angle = math.atan2(-1 * diff.y, diff.x) - math.radians(
                90
            )  # Angle to vertical axis

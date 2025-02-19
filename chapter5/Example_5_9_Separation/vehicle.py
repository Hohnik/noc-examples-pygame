# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

# Vehicle object


class Vehicle:
    def __init__(self, x, y):
        # All the usual stuff
        self.screen = pygame.display.get_surface()
        self.position = pygame.Vector2(x, y)
        self.acceleration = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        self.r = 12
        self.maxspeed = 1.5  # Maximum speed
        self.maxforce = 0.2  # Maximum steering force

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration += force

    # Separation
    # Method checks for nearby vehicles and steers away
    def separate(self, vehicles):
        # Note how the desired separation is based
        # on the Vehicle's size.
        desiredSeparation = self.r * 3
        sum = pygame.Vector2()
        count = 0
        for other in vehicles:
            d = self.position.distance_to(other.position)
            if d == 0:
                continue

            if self is not other and d < desiredSeparation:
                diff = self.position - other.position
                # What is the magnitude of the Vector
                # pointing away from the other vehicle?
                # The closer it is, the more the vehicle should flee.
                # The farther, the less. So the magnitude is set
                # to be inversely proportional to the distance.
                diff.scale_to_length(1 / d)
                sum += diff
                count += 1
        if count > 0:
            sum.scale_to_length(self.maxspeed)
            steer = sum - self.velocity
            steer.clamp_magnitude_ip(self.maxforce)
            self.applyForce(steer)

    # Method to update position
    def update(self):
        # Update velocity
        self.velocity += self.acceleration
        # Limit speed
        if self.velocity.length() > 0:
            self.velocity.scale_to_length(self.maxspeed)
        self.position += self.velocity
        # Reset accelerationelertion to 0 each cycle
        self.acceleration *= 0

    # Wraparound
    def borders(self):
        width, height = self.screen.get_width(), self.screen.get_height()
        if self.position.x < -self.r:
            self.position.x = width + self.r
        if self.position.y < -self.r:
            self.position.y = height + self.r
        if self.position.x > width + self.r:
            self.position.x = -self.r
        if self.position.y > width + self.r:
            self.position.y = -self.r

    def show(self):
        pygame.draw.aacircle(self.screen, "gray50", self.position, self.r / 2)
        pygame.draw.aacircle(self.screen, "black", self.position, self.r / 2, 1)

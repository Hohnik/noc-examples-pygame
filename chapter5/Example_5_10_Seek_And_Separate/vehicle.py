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
        self.maxspeed = 3  # Maximum speed
        self.maxforce = 0.2  # Maximum steering force
        self.r = 6

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration += force

    def applyBehaviors(self, vehicles):
        separateForce = self.separate(vehicles)
        seekForce = self.seek(pygame.Vector2(*pygame.mouse.get_pos()))

        separateForce *= 1.5
        seekForce *= 0.5

        self.applyForce(separateForce)
        self.applyForce(seekForce)

    # Separation
    # Method checks for nearby vehicles and steers away
    def separate(self, vehicles):
        desiredSeparation = self.r * 2
        sum = pygame.Vector2()
        count = 0
        # For every vehicle in the system, check if it't too close
        for other in vehicles:
            d = self.position.distance_to(other.position)

            if self is not other and d < desiredSeparation:
                diff = self.position - other.position
                diff.scale_to_length(1 / d)  # Weight by distance
                sum += diff
                count += 1  # Keep track of how many

        # Average -- device by how many
        if count > 0:
            sum /= count
            # Our desired vector is the average scaled to maximum speed
            sum.scale_to_length(self.maxspeed)
            # Implement Reynolds: Steering = Desired - Velocity
            sum -= self.velocity
            sum.clamp_magnitude_ip(self.maxforce)

        return sum

    # A method that calculates a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def seek(self, target):
        desired = (
            target - self.position
        )  # A vector pointing from the location to the target

        # Normalize desired and scale to maximum speed
        desired.normalize_ip()
        desired *= self.maxspeed

        # Steering = Desired minus velocity
        steer = desired - self.velocity
        steer.clamp_magnitude_ip(self.maxforce)  # Limit to maximum steering force
        return steer

    # Method to update position
    def update(self):
        # Update velocity
        self.velocity += self.acceleration
        # Limit speed
        self.velocity.clamp_magnitude_ip(self.maxspeed)
        self.position += self.velocity
        # Reset acceleration to 0 each cycle
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

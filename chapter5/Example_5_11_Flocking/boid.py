# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from random import random

import pygame

# Boid class
# Methods for Separation, Cohesion, Alignment added


class Boid:
    def __init__(self, x, y):
        self.screen = pygame.display.get_surface()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random() * 2 - 1, random() * 2 - 1)
        self.acceleration = pygame.Vector2()
        self.r = 3
        self.maxspeed = 3  # Maximum speed
        self.maxforce = 0.05  # Maximum steering force

    def run(self, boids):
        self.flock(boids)
        self.update()
        self.borders()
        self.show()

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration += force

    def flock(self, boids):
        sep = self.separate(boids)  # Separation
        ali = self.align(boids)  # Alignment
        coh = self.cohere(boids)  # Cohesion

        # Arbitrarily weight these forces
        sep *= 1.5
        ali *= 1.0
        coh *= 1.0

        # Add the force vecotrs to acceleration
        self.applyForce(sep)
        self.applyForce(ali)
        self.applyForce(coh)

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity += self.acceleration
        # Limit speed
        self.velocity.clamp_magnitude_ip(self.maxspeed)
        self.position += self.velocity
        # Reset acceleration to 0 each cycle
        self.acceleration *= 0

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

    def show(self):
        # Draw a triangle rotated in the direction of velocity
        angle = self.velocity.as_polar()[1]

        head = pygame.Vector2(self.r * 2, 0).rotate(angle)
        back_left = pygame.Vector2(-self.r * 2, -self.r).rotate(angle)
        back_right = pygame.Vector2(-self.r * 2, self.r).rotate(angle)

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

    # Wraparound
    def borders(self):
        width, height = self.screen.size
        if self.position.x < -self.r:
            self.position.x = width + self.r
        if self.position.y < -self.r:
            self.position.y = height + self.r
        if self.position.x > width + self.r:
            self.position.x = -self.r
        if self.position.y > height + self.r:
            self.position.y = -self.r

    # Separation
    # Method checks for nearby boids and steers away
    def separate(self, boids):
        desiredSeparation = 25
        steer = pygame.Vector2()
        count = 0

        # For every boid in the system, check if it't too close
        for other in boids:
            d = self.position.distance_to(other.position)

            # If the distance is greater thatn 0 and less than an arbitrary amount (0 when you are yourself)
            if d > 0 and d < desiredSeparation:
                # Calculate vector pointing away from neighbor
                diff = self.position - other.position
                diff.normalize_ip()
                diff /= d  # Weight by distance
                steer += diff
                count += 1  # Keep track of how many

        # Average -- device by how many
        if count > 0:
            steer /= count

        # As long as the vector is greater than 0
        if steer.magnitude() > 0:
            # Implement Reynolds: Steering = Desired - Velocity
            steer.normalize_ip()
            steer *= self.maxspeed
            steer -= self.velocity
            steer.clamp_magnitude_ip(self.maxforce)

        return steer

    # Alignment
    # For every nearby boid in the system, calculate the average velocity
    def align(self, boids):
        neighborDistance = 50
        sum = pygame.Vector2()
        count = 0

        for other in boids:
            d = self.position.distance_to(other.position)
            if d > 0 and d < neighborDistance:
                sum += other.velocity
                count += 1

        if count > 0:
            sum /= count
            sum.normalize_ip()
            sum *= self.maxspeed
            steer = sum - self.velocity
            steer.clamp_magnitude_ip(self.maxforce)
            return steer
        else:
            return pygame.Vector2()

    # Cohesion
    # For the average location (i.e. center) of all nearby boids, calculate steering vecotr towards that location
    def cohere(self, boids):
        neighborDistance = 50
        sum = pygame.Vector2()  # Start with empty vector to accumulate all locations
        count = 0

        for other in boids:
            d = self.position.distance_to(other.position)
            if d > 0 and d < neighborDistance:
                sum += other.position  # Add location
                count += 1

        if count > 0:
            sum /= count
            return self.seek(sum)  # Steer towards the location
        else:
            return pygame.Vector2()

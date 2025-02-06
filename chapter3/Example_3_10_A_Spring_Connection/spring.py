# Nature of Code
# Daniel Shiffman
# Chapter 3: Oscillation

import pygame

# Object to describe an anchor point that can connect to "Bob" objects via a spring
# Thank you: http://www.myphysicslab.com/spring2d.html


class Spring:
    def __init__(self, screen, x, y, length):
        self.screen = screen
        self.anchor = pygame.Vector2(x, y)
        self.restLength = length
        self.k = 0.2

    # Calculate and apply spring force
    def connect(self, bob):
        # Vector pointing from anchor to bob location
        force = bob.position - self.anchor
        # What is distance
        currentLength = force.magnitude()
        # Stretch is difference between current distance and rest length
        stretch = currentLength - self.restLength

        # Direction and magnitude together!
        force.scale_to_length(-1 * self.k * stretch)

        # Call applyForce() right here!
        bob.applyForce(force)

    def constrainLength(self, bob, minlen, maxlen):
        # Vector pointing from Bob to Anchor
        direction = bob.position - self.anchor
        length = direction.magnitude()

        # Is it too short?
        if length < minlen:
            direction.scale_to_length(minlen)
            # Keep position within constraint.
            bob.position = self.anchor + direction
            bob.velocity *= 0
            # Is it too long?
        elif length > maxlen:
            direction.scale_to_length(maxlen)
            # Keep position within constraint.
            bob.position = self.anchor + direction
            bob.velocity *= 0

    # Draw the anchor.
    def show(self):
        pygame.draw.circle(self.screen, "gray50", self.anchor, 5)
        pygame.draw.circle(self.screen, "black", self.anchor, 5, 1)

    # Draw the spring connection between Bob position and anchor.
    def showLine(self, bob):
        pygame.draw.aaline(self.screen, "black", bob.position, self.anchor)

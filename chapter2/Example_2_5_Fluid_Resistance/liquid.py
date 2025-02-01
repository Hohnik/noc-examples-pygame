# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
import pygame


class Liquid:
    def __init__(self, screen, x, y, w, h, c):
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    # Is the Mover in the Liquid?
    def contains(self, mover):
        pos = mover.position
        return (
            pos.x > self.x
            and pos.x < self.x + self.w
            and pos.y > self.y
            and pos.y < self.y + self.h
        )

    # Calculate drag force
    def calculateDrag(self, mover):
        # Magnitude is coefficient * speed squared
        speed = mover.velocity.magnitude()
        dragMagnitude = self.c * speed * speed

        # Direction is inverse of velocity
        dragForce = mover.velocity.copy()
        dragForce *= -1

        # Scale according to magnitude
        dragForce.scale_to_length(dragMagnitude)
        return dragForce

    def show(self):
        pygame.draw.rect(self.screen, "gray85", (self.x, self.y, self.w, self.h))

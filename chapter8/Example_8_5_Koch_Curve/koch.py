# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math

import pygame

# Koch Curve
# A class to describe one line segment in the fractal
# Includes methods to calculate midVectors along the line according to the Koch algorithm


class KochLine:
    def __init__(self, a, b):
        self.screen = pygame.display.get_surface()
        # Two pygame.Vector2's,
        # start is the "left" pygame.Vector2 and
        # end is the "right pygame.Vector2
        self.start = a.copy()
        self.end = b.copy()

    def show(self):
        pygame.draw.line(
            self.screen,
            "black",
            (self.start.x, self.start.y),
            (self.end.x, self.end.y),
            2,
        )

    def kochPoints(self):
        # Just the first point!
        a = self.start.copy()
        # Just the last point!
        e = self.end.copy()

        # A vector pointing in the direction, 1/3rd the length
        v = self.end - self.start
        v *= 1 / 3

        # b is just 1/3 of the way
        b = a + v
        # d is just another 1/3 of the way
        d = b + v

        # Rotate by -PI/3 radians (negative angle so it rotates "up").
        v.rotate_ip(-math.pi / 3)
        # Move along
        c = b + v

        # Return all five points in an array
        return [a, b, c, d, e]

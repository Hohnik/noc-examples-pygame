import pygame

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Pathfinding w/ Genetic Algorithms

# A class for an obstacle, just a simple rectangle that is drawn
# and can check if a Rocket touches it

# Also using this class for target position


class Obstacle:
    def __init__(self, x, y, w, h):
        self.screen = pygame.display.get_surface()
        self.position = pygame.Vector2(x, y)
        self.w = w
        self.h = h

    def show(self):
        assert self.screen
        pygame.draw.rect(
            self.screen, "gray50", (self.position.x, self.position.y, self.w, self.h)
        )
        pygame.draw.rect(
            self.screen, "black", (self.position.x, self.position.y, self.w, self.h), 1
        )

    def contains(self, spot):
        return (
            spot.x > self.position.x
            and spot.x < self.position.x + self.w
            and spot.y > self.position.y
            and spot.y < self.position.y + self.h
        )

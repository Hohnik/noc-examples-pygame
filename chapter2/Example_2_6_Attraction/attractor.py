# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math

import pygame

# An object for a draggable attractive body in our world

G = 1


class Attractor:
    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.position = pygame.Vector2(self.width / 2, self.height / 2)
        self.mass = 20
        self.dragOffset = pygame.Vector2()
        self.dragging = False
        self.rollover = False

    def attract(self, mover):
        # Calculate direction of force
        force = self.position - mover.position
        # Distance between objects
        distance = force.magnitude()
        # Limiting the distance to eliminate "extreme" results for very close or very far objects
        distance = pygame.math.clamp(distance, 5, 25)

        # Calculate gravitional force magnitude
        strength = (G * self.mass * mover.mass) / (distance * distance)
        # Get force vector --> magnitude * direction
        force.scale_to_length(strength)
        return force

    # Method to display
    def show(self):
        color = None
        if self.dragging:
            color = (50, 50, 50)
        elif self.rollover:
            color = (100, 100, 100)
        else:
            color = (175, 175, 175)

        pygame.draw.aacircle(self.screen, color, self.position, self.mass)
        pygame.draw.aacircle(self.screen, (0, 0, 0), self.position, self.mass, 4)

    # The methods below are for mouse interaction
    def handlePress(self, mx, my):
        d = dist(mx, my, self.position.x, self.position.y)
        if d < self.mass:
            self.dragging = True
            self.dragOffset.x = self.position.x - mx
            self.dragOffset.y = self.position.y - my

    def handleHover(self, mx, my):
        d = dist(mx, my, self.position.x, self.position.y)
        if d < self.mass:
            self.rollover = True
        else:
            self.rollover = False

    def stopDragging(self):
        self.dragging = False

    def handleDrag(self, mx, my):
        if self.dragging:
            self.position.x = mx + self.dragOffset.x
            self.position.y = my + self.dragOffset.y


def dist(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)

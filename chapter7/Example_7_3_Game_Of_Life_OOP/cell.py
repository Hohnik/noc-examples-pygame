# The Nature of
# Daniel Shiffman
# http://natureofcode.com

import pygame


class Cell:
    def __init__(self, state, x, y, w):
        self.screen = pygame.display.get_surface()

        # What is the cell’s state?
        self.state = state
        self.previous = self.state

        # position and size
        self.x = x
        self.y = y
        self.w = w

    def show(self):
        color = None
        # If the cell is born, color it blue!
        if self.previous == 0 and self.state == 1:
            color = (0, 0, 255)
        elif self.state == 1:
            color = (0, 0, 0)
            # If the cell dies, color it red!
        elif self.previous == 1 and self.state == 0:
            color = (255, 0, 0)
        else:
            color = (255, 255, 255)

        pygame.draw.rect(self.screen, color, (self.x, self.y, self.w, self.w))
        pygame.draw.rect(self.screen, "black", (self.x, self.y, self.w, self.w), 1)

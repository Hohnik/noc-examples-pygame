# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import math


class Turtle:
    def __init__(self, length, angle):
        self.length = length
        self.angle = angle

    def render(self, screen, sentence, start_pos, start_angle):
        stack = []
        x, y = start_pos
        angle = start_angle

        for c in sentence:
            if c in "FG":
                new_x = x + self.length * math.cos(angle)
                new_y = y - self.length * math.sin(angle)
                pygame.draw.aaline(screen, (0, 0, 0), (x, y), (new_x, new_y), 1)
                x, y = new_x, new_y
            elif c == "+":
                angle += self.angle
            elif c == "-":
                angle -= self.angle
            elif c == "[":
                stack.append((x, y, angle))
            elif c == "]":
                x, y, angle = stack.pop()

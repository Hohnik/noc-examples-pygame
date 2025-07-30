# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import math

from lsystem import LSystem
from _turtle import Turtle  # _ here becuase turtle is a official library


def setup(screen):
    screen.fill("white")

    rules = {"F": "FF+[+F-F-F]-[-F+F+F]"}
    lsystem = LSystem("F", rules)
    turtle = Turtle(4, math.radians(25))

    for _ in range(4):
        lsystem.generate()

    # Some other rules
    # ruleset = {"F": "F[F]-F+F[--F]+F-F"}
    # lsystem = LSystem("F-F-F-F", ruleset)
    # turtle = Turtle(4, math.pi / 2)

    # ruleset = {
    #   "F": "F--F--F--G",
    #   "G": "GG",
    # }
    # lsystem = LSystem("F--F--F", ruleset)
    # turtle = Turtle(8, math.pi / 3)

    # Draw the L-system using the turtle
    # Start at bottom center, facing up
    start_pos = (screen.get_width() // 2, screen.get_height())  # Bottom center
    start_angle = math.pi / 2  # Up angle
    turtle.render(screen, lsystem.sentence, start_pos, start_angle)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 240))
    setup(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

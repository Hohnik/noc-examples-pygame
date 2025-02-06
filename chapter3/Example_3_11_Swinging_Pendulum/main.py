# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from pendulum import Pendulum

# Pendulum

# A simple pendulum simulation
# Given a pendulum with an angle theta (0 being the pendulum at rest) and a radius r
# we can use sine to calculate the angular component of the gravitational force.

# Gravity Force = Mass * Gravitational Constant;
# Pendulum Force = Gravity Force * sine(theta)
# Angular Acceleration = Pendulum Force / Mass = gravitational acceleration * sine(theta);

# Note this is an ideal world scenario with no tension in the
# pendulum arm, a more realistic formula might be:
# Angular Acceleration = (g / R) * sine(theta)

# For a more substantial explanation, visit:
# http://www.myphysicslab.com/pendulum1.htmlimport pygame

running = True

pendulum = None


def setup():
    global pendulum
    screen = pygame.display.set_mode((640, 360))
    # Make a new Pendulum with an origin position and armlength
    pendulum = Pendulum(screen, screen.get_width() / 2, 0, 175)
    return screen


def draw(screen: pygame.Surface):
    global pendulum, running
    screen.fill("white")

    pendulum.update()
    pendulum.show()

    pendulum.drag()  # For user interaction

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pendulum.clicked(*pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:
            pendulum.stopDragging()


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    screen = setup()

    while running:
        draw(screen)

        pygame.display.flip()
        clock.tick(60)

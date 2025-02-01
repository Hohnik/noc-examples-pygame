# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from random import random

import pygame
from mover import Body

bodies = [None for i in range(10)]


def setup():
    global bodies
    screen = pygame.display.set_mode((640, 360))
    width, height = screen.get_width(), screen.get_height()
    for i in range(len(bodies)):
        bodies[i] = Body(
            screen, random() * width, random() * height, random() * 1.9 + 0.1
        )
    return screen


def draw(screen):
    global bodies
    screen.fill((255, 255, 255))

    for bodyA in bodies:
        for bodyB in bodies:
            if bodyA != bodyB:
                force = bodyB.attract(bodyA)
                bodyA.applyForce(force)

        bodyA.update()
        bodyA.show()


if __name__ == "__main__":
    pygame.init()
    screen = setup()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw(screen)

        pygame.display.flip()
        clock.tick(100)

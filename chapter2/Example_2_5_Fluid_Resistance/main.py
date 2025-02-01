# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import random

import pygame
from liquid import Liquid
from mover import Mover

# Forces (Gravity and Fluid Resistence) with Vectors

# Demonstration of multiple force acting on bodies (Mover class)
# Bodies experience gravity continuously
# Bodies experience fluid resistance when in "water"

# Five moving bodies
movers: list[Mover] = []

# Liquid
liquid = None


def setup():
    global liquid
    screen = pygame.display.set_mode((640, 360))
    reset(screen)
    # Create liquid object
    width, height = screen.get_width(), screen.get_height()
    liquid = Liquid(screen, 0, height / 2, width, height / 2, 0.1)
    return screen


def draw(screen):
    global liquid, movers
    screen.fill((255, 255, 255))

    # Draw liquid
    liquid.show()

    for i in range(len(movers)):
        # Is the Mover in the liquid?
        if liquid.contains(movers[i]):
            # Calculate drag force
            dragForce = liquid.calculateDrag(movers[i])
            # Apply drag force to Mover
            movers[i].applyForce(dragForce)

        # Gravity is scaled by mass here!
        gravity = pygame.Vector2(0, 0.1 * movers[i].mass)
        # Apply gravity
        movers[i].applyForce(gravity)

        # Update and display
        movers[i].update()
        movers[i].show()
        movers[i].checkEdges()


def reset(screen):
    global movers
    movers = []
    for i in range(9):
        movers.append(Mover(screen, 40 + i * 70, 0, random.random() * 2.5 + 0.5))


if __name__ == "__main__":
    pygame.init()
    screen = setup()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                reset(screen)

        draw(screen)

        pygame.display.flip()
        clock.tick(60)

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from mover import Mover

mover = None


def setup():
    global mover
    screen = pygame.display.set_mode((640, 360))
    mover = Mover(screen)
    return screen


def draw(screen):
    global mover
    screen.fill((255, 255, 255))

    mover.update()
    mover.checkEdges()
    mover.display()


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
        clock.tick(60)

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
    print("Click mouse to apply wind force")
    return screen


def draw(screen):
    global mover
    screen.fill((255, 255, 255))

    gravity = pygame.Vector2(0, 0.1)
    mover.applyForce(gravity)

    if pygame.mouse.get_pressed()[0]:
        wind = pygame.Vector2(0.1, 0)
        mover.applyForce(wind)

    mover.update()
    mover.checkEdges()
    mover.show()


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

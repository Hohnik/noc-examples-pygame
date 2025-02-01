# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from mover import Mover

moverA = None
moverB = None


def setup():
    global moverA, moverB
    screen = pygame.display.set_mode((640, 360))
    # A large Mover on the left side of the window
    moverA = Mover(screen, 200, 30, 10)
    # A smaller Mover on the right side of the window
    moverB = Mover(screen, 440, 30, 2)
    print("Click mouse to apply wind force")
    return screen


def draw(screen):
    global moverA, moverB
    screen.fill((255, 255, 255))

    gravity = pygame.Vector2(0, 0.1)

    gravityA = gravity * moverA.mass
    moverA.applyForce(gravityA)

    gravityB = gravity * moverB.mass
    moverB.applyForce(gravityB)

    if pygame.mouse.get_pressed()[0]:
        wind = pygame.Vector2(0.1, 0)
        moverA.applyForce(wind)
        moverB.applyForce(wind)

    moverA.update()
    moverA.display()
    moverA.checkEdges()

    moverB.update()
    moverB.display()
    moverB.checkEdges()


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

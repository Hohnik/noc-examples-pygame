# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com


import pygame
from mover import Body

bodyA = None
bodyB = None


def setup():
    global bodyA, bodyB
    screen = pygame.display.set_mode((640, 360))
    bodyA = Body(screen, 320, 60)
    bodyB = Body(screen, 320, 300)
    bodyA.velocity = pygame.Vector2(1, 0)
    bodyB.velocity = pygame.Vector2(-1, 0)
    return screen


def draw(screen):
    global bodyA, bodyB
    screen.fill((255, 255, 255))

    bodyA.attract(bodyB)
    bodyB.attract(bodyA)

    bodyA.update()
    bodyA.show()
    bodyB.update()
    bodyB.show()


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

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from mover import Mover

mover = None


def setup():
    global mover
    screen = pygame.display.set_mode((640, 360))
    mover = Mover(screen, screen.get_width() / 2, 30, 5)
    print("Click mouse to apply wind force")
    return screen


def draw(screen):
    global mover
    screen.fill((255, 255, 255))

    gravity = pygame.Vector2(0, 1)
    # {!1} I should scale by mass to be more accurate, but this example only has one circle
    mover.applyForce(gravity)

    if pygame.mouse.get_pressed()[0]:
        wind = pygame.Vector2(0.5, 0)
        mover.applyForce(wind)

    if mover.contactEdge():
        # {!5 .bold}
        c = 0.1
        friction = mover.velocity.copy()
        friction *= -1
        friction.scale_to_length(c)

        # {!1 .bold} Apply the friction force vector to the object.
        mover.applyForce(friction)

    mover.bounceEdges()
    mover.update()
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

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from attractor import Attractor
from mover import Mover

running = True
mover = None
attractor = None
mousePressed = False


def setup():
    global mover, attractor
    screen = pygame.display.set_mode((640, 360))
    mover = Mover(screen, 300, 70, 2)
    attractor = Attractor(screen)
    return screen


def draw(screen):
    global attractor, movers, mousePressed, running
    screen.fill((255, 255, 255))

    force = attractor.attract(mover)
    mover.applyForce(force)
    mover.update()

    attractor.show()
    mover.show()

    for event in pygame.event.get():
        mouseX, mouseY = pygame.mouse.get_pos()

        if not mousePressed and event.type == pygame.MOUSEMOTION:
            attractor.handleHover(mouseX, mouseY)

        if not mousePressed and event.type == pygame.MOUSEBUTTONDOWN:
            mousePressed = True
            attractor.handlePress(mouseX, mouseY)

        if mousePressed and event.type == pygame.MOUSEMOTION:
            attractor.handleHover(mouseX, mouseY)
            attractor.handleDrag(mouseX, mouseY)

        if mousePressed and event.type == pygame.MOUSEBUTTONUP:
            mousePressed = False
            attractor.stopDragging()

        if event.type == pygame.QUIT:
            running = False


if __name__ == "__main__":
    pygame.init()
    screen = setup()
    clock = pygame.time.Clock()

    while running:
        draw(screen)

        pygame.display.flip()
        clock.tick(60)

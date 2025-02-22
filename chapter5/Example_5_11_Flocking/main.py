# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from boid import Boid
from flock import Flock

flock = None


def setup():
    global flock
    screen = pygame.display.set_mode((640, 360))
    width, height = screen.size
    flock = Flock()
    # Add an initial set of boids into the system
    for i in range(120):
        boid = Boid(width / 2, height / 2)
        flock.addBoid(boid)
    return screen


def draw(screen: pygame.Surface):
    global debug, vehicles, flowfield
    screen.fill((255, 255, 255))

    flock.run()

    # Add a new boid into the System
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        flock.addBoid(Boid(mouseX, mouseY))


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = setup()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw(screen)
        pygame.display.flip()
        clock.tick(60)

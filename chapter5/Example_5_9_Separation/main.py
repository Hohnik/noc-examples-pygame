# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from random import random

import pygame
from vehicle import Vehicle

# Separation
# Via Reynolds: http://www.red3d.com/cwr/steer/

# A list of vehicles
vehicles = []


def setup():
    global vehicles
    screen = pygame.display.set_mode((640, 360))

    for i in range(25):
        vehicles.append(
            Vehicle(random() * screen.get_width(), random() * screen.get_height())
        )

    return screen


def draw(screen: pygame.Surface):
    global vehicles
    screen.fill((255, 255, 255))

    for v in vehicles:
        v.separate(vehicles)
        v.update()
        v.borders()
        v.show()

    if pygame.mouse.get_just_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        vehicles.append(Vehicle(mouseX, mouseY))


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

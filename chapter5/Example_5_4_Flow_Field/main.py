# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from random import random

import pygame
from flowfield import FlowField
from vehicle import Vehicle

## Flow Field Following
## Via Reynolds: http://www.red3d.com/cwr/steer/FlowFollow.html

## Using this variable to decide whether to draw all the stuff
debug = True

# Flowfield object
flowfield = None

# A List of vehicles
vehicles = []


def setup():
    global vehicles, flowfield
    screen = pygame.display.set_mode((640, 360))

    print(
        "Hit space bar to toggle debugging lines.\nClick the mouse to generate a new flow field."
    )
    # Make a new flow field with "resolution" of 16
    flowfield = FlowField(screen, 20)
    # Make a whole bunch of vehicles with random maxspeed and maxforce values
    for i in range(120):
        vehicles.append(
            Vehicle(
                screen,
                random() * screen.get_width(),
                random() * screen.get_height(),
                random() * 3 + 2,
                random() * 0.4 + 0.1,
            )
        )
    return screen


def draw(screen: pygame.Surface):
    global debug, vehicles, flowfield
    screen.fill((255, 255, 255))

    # Displaay the flowfield in "debug" mode
    if debug:
        flowfield.show()

    # Tell all the vehicles to follow the flow field
    for vehicle in vehicles:
        vehicle.follow(flowfield)
        vehicle.run()

    # Make a new flowfield
    if pygame.mouse.get_just_pressed()[0]:
        flowfield.init()

    if pygame.key.get_just_pressed()[pygame.K_SPACE]:
        debug = not debug


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

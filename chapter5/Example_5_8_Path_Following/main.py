# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from random import randint as random

import pygame
from path import Path
from vehicle import Vehicle

# Path Following
# Path is a just a straight line in this example
# Via Reynolds: // http://www.red3d.com/cwr/steer/PathFollow.html

# Using this variable to decide whether to draw all the stuff
debug = True

# A path object (series of connected points)
path = None

# Two vehicles
car1, car2 = None, None


def setup():
    global car1, car2, path
    screen = pygame.display.set_mode((640, 360))
    print(
        "Hit space bar to toggle debugging lines.\nClick the mouse to generate a new path"
    )

    path = newPath()

    # Each vehicle has different maxspeed and maxforce for demo purposes
    car1 = Vehicle(0, screen.get_height() / 2, 2, 0.04)
    car2 = Vehicle(0, screen.get_height() / 2, 3, 0.1)
    return screen


def draw(screen: pygame.Surface):
    global path, car1, car2
    screen.fill((255, 255, 255))

    # Display the path
    path.show()

    # The boids follow the path
    car1.follow(path)
    car2.follow(path)

    # Call the generic run method (udpate, borders, display, etc.)
    car1.run()
    car2.run()

    # Check if it gets to the end of the path since it's not a loop
    car1.borders(path)
    car2.borders(path)

    if pygame.mouse.get_just_pressed()[0]:
        path = newPath()


def newPath():
    screen = pygame.display.get_surface()
    width, height = screen.get_width(), screen.get_height()
    # A path is a series of connected points
    # A more sophisticated path might be a curve
    path = Path()
    path.addPoint(-20, height / 2)
    path.addPoint(random(0, width // 2), random(0, height))
    path.addPoint(random(width // 2, width), random(0, height))
    path.addPoint(width + 20, height // 2)
    return path


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

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

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
vehicle1, vehicle2 = None, None


def setup():
    global vehicle1, vehicle2, path
    screen = pygame.display.set_mode((640, 360))

    path = Path()

    # Each vehicle has different maxspeed and maxforce for demo purposes
    vehicle1 = Vehicle(0, screen.get_height() / 2, 2, 0.02)
    vehicle2 = Vehicle(0, screen.get_height() / 2, 3, 0.05)
    print("Hit space bar to toggle debugging lines.")
    return screen


def draw(screen: pygame.Surface):
    global path, vehicle1, vehicle2
    screen.fill((255, 255, 255))

    # Display the path
    path.show()

    # The boids follow the path
    vehicle1.follow(path)
    vehicle2.follow(path)

    # Call the generic run method (udpate, borders, display, etc.)
    vehicle1.run()
    vehicle2.run()

    # Check if it gets to the end of the path since it's not a loop
    vehicle1.borders(path)
    vehicle2.borders(path)


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

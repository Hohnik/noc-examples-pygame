# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from vehicle import Vehicle

# Stay Within Walls
# "Made-up" Steering behavior to stay within walls


vehicle = None

debug = True
offset = 25


def setup():
    global vehicle
    screen = pygame.display.set_mode((640, 360))
    vehicle = Vehicle(screen, screen.get_width() / 2, screen.get_height() / 2)
    return screen


def draw(screen: pygame.Surface):
    screen.fill((255, 255, 255))

    if debug:
        width, height = screen.get_width(), screen.get_height()
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (offset, offset, width - 2 * offset, height - 2 * offset),
            2,
        )

    # Call the appropriate steering behaviors for our agents
    vehicle.boundaries(offset)

    vehicle.update()
    vehicle.show()


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

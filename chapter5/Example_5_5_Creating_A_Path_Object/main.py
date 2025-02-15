# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from path import Path

# Path Following
# Path is a just a straight line in this example
# Via Reynolds: // http://www.red3d.com/cwr/steer/PathFollow.html
#
# A path object (series of connected points)
path = None


def setup():
    global path
    screen = pygame.display.set_mode((640, 360))
    path = Path(screen)
    return screen


def draw(screen: pygame.Surface):
    global path
    screen.fill((255, 255, 255))
    path.show()


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

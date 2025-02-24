# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

# Simple Recursion


def setup():
    screen = pygame.display.set_mode((640, 360))
    screen.fill((255, 255, 255))
    width, height = screen.size
    drawCircles(width / 2, height / 2, 320)


def drawCircles(x, y, radius):
    screen = pygame.display.get_surface()
    pygame.draw.aacircle(screen, "black", (x, y), radius, 2)

    if radius > 4:
        # drawCircles() calls itself twice.
        # For each circle, a smaller circle is drawn to the left and the right
        drawCircles(x + radius / 2, y, radius / 2)
        drawCircles(x - radius / 2, y, radius / 2)


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    setup()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        clock.tick(60)

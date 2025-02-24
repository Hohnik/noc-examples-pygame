# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

# Simple Recursion


def setup():
    screen = pygame.display.set_mode((640, 360))
    screen.fill((255, 255, 255))
    width, height = screen.size
    drawCircles(width / 2, height / 2, width / 2)


# Very simple function that draws one circle
# and recursively calls itself
def drawCircles(x, y, r):
    screen = pygame.display.get_surface()
    pygame.draw.aacircle(screen, "black", (x, y), r, 1)

    # Exit condition, stop when radius is too small
    if r > 4:
        r *= 0.618
        # Call the function inside the function! (recursion!)
        drawCircles(x, y, r)


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

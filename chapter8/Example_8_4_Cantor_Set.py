# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

# Cantor Set
# Renders a simple fractal, the Cantor Set


def setup():
    screen = pygame.display.set_mode((640, 120))
    screen.fill((255, 255, 255))
    width, height = screen.size

    # Call the recursive function
    cantor(10, 10, 620)


def cantor(x, y, length):
    screen = pygame.display.get_surface()

    # Stop at 1 pixel!
    if length > 1:
        pygame.draw.line(screen, "black", (x, y), (x + length, y))
        cantor(x, y + 20, length / 3)
        cantor(x + (2 * length) / 3, y + 20, length / 3)


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

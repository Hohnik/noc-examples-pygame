# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

# Example 1-4: Vector multiplication


def setup():
    screen = pygame.display.set_mode((640, 360))
    return screen


def draw(screen: pygame.Surface):
    screen.fill((255, 255, 255))

    mouse = pygame.Vector2(pygame.mouse.get_pos())
    center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    pygame.draw.line(screen, "gray80", (center), (mouse), 4)

    # {!1} Multiplying a vector!  The vector is now half its original size (multiplied by 0.5).
    mouse *= 0.5

    pygame.draw.line(screen, "black", (center), (mouse + 0.5 * center), 4)


if __name__ == "__main__":
    pygame.init()
    screen = setup()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw(screen)

        pygame.display.flip()
        clock.tick(60)

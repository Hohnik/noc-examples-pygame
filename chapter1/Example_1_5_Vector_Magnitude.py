# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

# Example 1-5: Vector magnitude


def setup():
    screen = pygame.display.set_mode((640, 360))
    return screen


def draw(screen: pygame.Surface):
    screen.fill((255, 255, 255))

    mouse = pygame.Vector2(pygame.mouse.get_pos())
    center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    # {!3} The magnitude (i.e. length) of a vector can be accessed via the magnitude() function.  Here it is used as the width of a rectangle drawn at the top of the window.
    m = (mouse - center).magnitude()
    pygame.draw.rect(screen, "black", (10, 10, m, 10))

    pygame.draw.line(screen, "black", (center), (mouse))


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

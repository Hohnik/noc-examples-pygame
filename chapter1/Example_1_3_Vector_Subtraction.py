# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

# Example 1-3: Vector subtraction


def setup():
    screen = pygame.display.set_mode((640, 360))
    return screen


def draw(screen: pygame.Surface):
    screen.fill((255, 255, 255))

    # Two vectors, one for the mouse position and one for the center of the window
    mouse = pygame.Vector2(pygame.mouse.get_pos())
    center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    # Draw the original two vectors
    pygame.draw.line(screen, "gray80", (0, 0), (mouse), 4)
    pygame.draw.line(screen, "gray80", (0, 0), (center), 4)

    # Vector subtraction!
    mouse -= center

    # Draw a line to represent the result of subtraction.
    pygame.draw.line(screen, "black", (center), (mouse + center), 4)


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

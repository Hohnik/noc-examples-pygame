# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

# Example 1-6: Vector normalizing
# Demonstration of normalizing a vector.
# Normalizing a vector sets its length to 1.


def setup():
    screen = pygame.display.set_mode((640, 360))
    return screen


def draw(screen: pygame.Surface):
    screen.fill((255, 255, 255))

    # A vector that points to the mouse position
    mouse = pygame.Vector2(pygame.mouse.get_pos())
    #  A vector that points to the center of the window
    center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    # Subtract center from mouse which results in a vector that points from center to mouse
    v = mouse - center

    pygame.draw.line(screen, "gray80", (center), (mouse), 2)

    # Normalize the vector
    v.normalize_ip()

    # Multiply its length by 50
    v *= 50

    # Draw the resulting vector
    pygame.draw.line(screen, "black", (center), (center + v), 8)


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

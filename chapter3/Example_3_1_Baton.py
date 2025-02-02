# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

angle = 0


def setup():
    screen = pygame.display.set_mode((640, 360))
    return screen


def draw(screen: pygame.Surface):
    global angle
    screen.fill((255, 255, 255))
    center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    p1, p2 = pygame.Vector2(-50, 0), pygame.Vector2(50, 0)
    p1 = p1.rotate_rad(angle)
    p2 = p2.rotate_rad(angle)

    pygame.draw.aaline(screen, "black", (p1 + center), (p2 + center))

    pygame.draw.aacircle(screen, "gray50", (p1 + center), 8)
    pygame.draw.aacircle(screen, "black", (p1 + center), 8, 1)

    pygame.draw.aacircle(screen, "gray50", (p2 + center), 8)
    pygame.draw.aacircle(screen, "black", (p2 + center), 8, 1)
    angle += 0.1


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

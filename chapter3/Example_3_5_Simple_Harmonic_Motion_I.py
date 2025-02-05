# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math

import pygame

frame_count = 0


def setup():
    screen = pygame.display.set_mode((640, 360))
    return screen


def draw(screen: pygame.Surface):
    global frame_count
    frame_count += 1
    screen.fill((255, 255, 255))
    center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    period = 120
    amplitude = 200

    # Calculating horizontal position according to formula for simple harmonic motion
    x = amplitude * math.sin((math.pi * frame_count) / period)

    pygame.draw.line(screen, "black", center, (x + center.x, center.y), 2)
    pygame.draw.aacircle(screen, "gray50", (x + center.x, center.y), 24)
    pygame.draw.aacircle(screen, "black", (x + center.x, center.y), 24, 1)


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

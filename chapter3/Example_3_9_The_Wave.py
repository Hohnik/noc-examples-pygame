# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math

import pygame

startAngle = 0
angleVelocity = 0.2


def setup():
    screen = pygame.display.set_mode((640, 360))
    return screen


def draw(screen):
    global startAngle, angleVelocity
    screen.fill((255, 255, 255))

    angle = startAngle
    startAngle += 0.02

    for x in range(0, screen.get_width(), 24):
        bg = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

        def remap(
            value, old_min, old_max, new_min, new_max
        ):  # this is equal to the map function in p5.js
            return new_min + (value - old_min) * (new_max - new_min) / (
                old_max - old_min
            )

        y = remap(math.sin(angle), -1, 1, 0, bg.get_height())
        pygame.draw.circle(bg, (127, 127, 127, 127), (x, y), 24)
        pygame.draw.circle(bg, (0, 0, 0, 127), (x, y), 24, 1)
        angle += angleVelocity

        screen.blit(bg)


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

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math

import pygame

angle = 0
angleVelocity = 0.2
amplitude = 100


def setup():
    global angle, angleVelocity, amplitude
    screen = pygame.display.set_mode((640, 360))
    screen.fill((255, 255, 255))

    for x in range(0, screen.get_width(), 24):
        # 1) Calculate the y position according to amplitude and sine of the angle.
        y = amplitude * math.sin(angle)

        # 2) Draw a circle at the (x,y) position.
        background = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        pygame.draw.circle(
            background, (127, 127, 127, 127), (x, y + background.get_height() / 2), 24
        )
        pygame.draw.circle(
            background, (0, 0, 0, 127), (x, y + background.get_height() / 2), 24, 1
        )
        screen.blit(background)
        # 3) Increment the angle according to angular velocity.
        angle += angleVelocity


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    setup()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

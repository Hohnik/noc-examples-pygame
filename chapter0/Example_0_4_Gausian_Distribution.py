# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import random

import pygame


def setup():
    screen = pygame.display.set_mode((640, 360))
    screen.fill((255, 255, 255))
    return screen


def draw(screen: pygame.Surface):
    x = random.gauss(320, 60)
    surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    pygame.draw.circle(surface,(0,0,0,10), (x,180), 16)
    screen.blit(surface, (0,0))


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

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import random

import pygame

randomCounts = [0 for _ in range(20)]
total = 20


def setup(screen): ...


def draw(screen):
    index = random.randint(0, total - 1)
    randomCounts[index] += 1

    w = screen.get_width() / len(randomCounts)

    for x in range(len(randomCounts)):
        rect = pygame.Rect(
            x * w, screen.get_height() - randomCounts[x], w - 1, randomCounts[x]
        )
        pygame.draw.rect(screen, (127, 127, 127), rect)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 360))
    screen.fill((255, 255, 255))
    clock = pygame.time.Clock()

    setup(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw(screen)

        pygame.display.flip()
        clock.tick(60)

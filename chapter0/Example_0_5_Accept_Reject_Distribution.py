# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import random

import pygame

randomCounts = [0 for _ in range(20)]

def setup():
    screen = pygame.display.set_mode((640, 360))
    screen.fill((255, 255, 255))
    return screen


def draw(screen):
    index = int(accept_reject() * len(randomCounts))
    randomCounts[index] += 1

    w = screen.get_width() / len(randomCounts)

    for x in range(len(randomCounts)):
        rect = pygame.Rect(
            x * w, screen.get_height() - randomCounts[x], w - 1, randomCounts[x]
        )
        pygame.draw.rect(screen, (127, 127, 127), rect)

def accept_reject():
    # We do this “forever” until we find a qualifying random value.
    while True:
        # Pick a random value.
        r1 = random.random()
        # Assign a probability.
        probability = r1
        # Pick a second random value.
        r2 = random.random()
        #{!3} Does it qualify?  If so, we’re done!
        if (r2 < probability):
              return r1

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

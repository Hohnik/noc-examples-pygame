# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from oscillator import Oscillator

# An array of objects
oscillators = []


def setup():
    global oscillators
    screen = pygame.display.set_mode((640, 360))
    # Initialize all objects
    for i in range(10):
        oscillators.append(Oscillator(screen))
    return screen


def draw(screen: pygame.Surface):
    global oscillators
    screen.fill((255, 255, 255))
    # Run all objects
    for oscillator in oscillators:
        oscillator.update()
        oscillator.show()


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

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import random

import pygame

walker = None


def setup(screen):
    global walker
    walker = Walker(screen)


def draw(screen):
    global walker
    walker.step()
    walker.show()


class Walker:
    def __init__(self, screen):
        self.screen = screen
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2

    def show(self):
        self.screen.set_at((self.x, self.y), 0)

    def step(self):
        choice = random.randint(0, 3)

        if choice == 0:
            self.x += 1
        elif choice == 1:
            self.x -= 1
        elif choice == 2:
            self.y += 1
        else:
            self.y -= 1


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

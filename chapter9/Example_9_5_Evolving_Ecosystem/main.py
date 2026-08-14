# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from world import World

# A World of creatures that eat food
# The more they eat, the longer they survive
# The longer they survive, the more likely they are to reproduce
# The bigger they are, the easier it is to land on food
# The bigger they are, the slower they are to find food
# When the creatures die, food is left behind


def setup(screen: pygame.Surface):
    global world

    # World starts with 20 bloops and 20 pieces of food
    world = World(20)


def draw(screen: pygame.Surface):
    screen.fill("white")

    world.run()


# We can add a creature mannually if we so desire
def handleMouseEvents(event: pygame.event.Event):
    if (
        event.type == pygame.MOUSEBUTTONDOWN
        or event.type == pygame.MOUSEMOTION
        and any(event.buttons)
    ):
        world.born(*event.pos)


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 240))
    setup(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            handleMouseEvents(event)
        draw(screen)
        pygame.display.update()
        clock.tick(60)

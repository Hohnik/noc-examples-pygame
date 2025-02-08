# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from emitter import Emitter

# Particles are generated each cycle through draw(),
# fall with gravity and fade out over time
# A ParticleSystem object manages a variable size
# list of particles.

emitter = None


def setup():
    global emitter
    screen = pygame.display.set_mode((640, 360))
    emitter = Emitter(screen, screen.get_width() / 2, 20)
    return screen


def draw(screen: pygame.Surface):
    global emitter
    screen.fill("white")
    emitter.addParticle()
    emitter.run()


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

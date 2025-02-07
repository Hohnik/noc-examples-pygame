# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from emitter import Emitter

# Particles are generated each cycle through draw(),
# fall with gravity and fade out over time
# A ParticleSystem object manages a variable size
# list of particles.

# an array of ParticleSystems
emitters = []


def setup():
    global emitter
    screen = pygame.display.set_mode((640, 360))
    print("click to add particle systems")
    return screen


def draw(screen: pygame.Surface):
    global emitters
    screen.fill("white")
    for emitter in emitters:
        emitter.run()
        emitter.addParticle()


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    screen = setup()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                emitters.append(Emitter(screen, mouseX, mouseY))

        draw(screen)

        pygame.display.flip()
        clock.tick(60)

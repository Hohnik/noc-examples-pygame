# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from emitter import Emitter
from repeller import Repeller

# One ParticleSystem
emitter = None

# One repeller
repeller = None


def setup():
    global emitter, repeller
    screen = pygame.display.set_mode((640, 360))
    emitter = Emitter(screen, screen.get_width() / 2, 50)
    repeller = Repeller(screen, screen.get_width() / 2, 250)
    return screen


def draw(screen: pygame.Surface):
    global emitter
    screen.fill("white")
    emitter.addParticle()
    # We're applying a universal gravity.
    gravity = pygame.Vector2(0, 0.1)
    emitter.applyForce(gravity)
    # Applying the repeller
    emitter.applyRepeller(repeller)
    emitter.run()
    repeller.show()


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

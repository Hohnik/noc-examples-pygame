# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from particle import Particle

particle = None


def setup():
    global particle
    screen = pygame.display.set_mode((640, 360))
    particle = Particle(screen, screen.get_width() / 2, 10)
    return screen


def draw(screen: pygame.Surface):
    global particle
    screen.fill("white")
    # Operating the single Particle
    particle.update()
    particle.show()

    # Applying a gravity force
    gravity = pygame.Vector2(0, 0.1)
    particle.applyForce(gravity)

    # Checking the particle's state and making a new particle
    if particle.isDead():
        particle = Particle(screen, screen.get_width() / 2, 20)
        print("Particle dead!")


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

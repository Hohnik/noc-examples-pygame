# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from particle import Particle

particles = []


def setup():
    screen = pygame.display.set_mode((640, 360))
    return screen


def draw(screen: pygame.Surface):
    global particle
    screen.fill("white")
    particles.append(Particle(screen, screen.get_width() / 2, 20))

    # Looping through backwards to delete
    for i in range(len(particles) - 1, -1, -1):
        particle = particles[i]
        particle.run()
        if particle.isDead():
            # remove the particle
            particles.pop(i)


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

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from emitter import Emitter
from utils import map_value

# Smoke Particle System

# A basic smoke effect using a particle system
# Each particle is rendered as an alpha masked image


emitter = None


def setup():
    global emitter, img
    screen = pygame.display.set_mode((640, 360))
    img = pygame.image.load("./data/texture.png")
    emitter = Emitter(screen, screen.get_width() / 2, screen.get_height() - 100, img)
    return screen


def draw(screen: pygame.Surface):
    global emitter
    # Try additive blending!
    # blendMode(ADD);
    screen.fill((0, 0, 0))

    # Wind force direction based on mouseX
    mouseX = pygame.mouse.get_pos()[0]
    dx = map_value(mouseX, 0, screen.get_width(), -0.2, 0.2)
    wind = pygame.Vector2(dx, 0)
    emitter.applyForce(wind)
    emitter.run()
    emitter.addParticle()

    # Draw an arrow representing the wind force
    start_position = pygame.Vector2(screen.get_width() / 2, 50)
    drawVector(screen, wind, start_position, 50)


def drawVector(screen, v, pos, scale):
    arrowsize = 4

    dir = 1
    if v.x < 0:
        dir = -1

    # Calculate length of vector & scale it to be bigger or smaller if necessary
    len = v.magnitude() * scale**1.8

    # Draw three lines to make an arrow (draw pointing up since we've rotate to the proper direction)
    pygame.draw.line(
        screen, "white", (0 + pos.x, 0 + pos.y), (len * dir + pos.x, 0 + pos.y), 2
    )
    pygame.draw.line(
        screen,
        "white",
        (len * dir + pos.x, 0 + pos.y),
        (len * dir - arrowsize * dir + pos.x, +arrowsize / 2 + pos.y),
        2,
    )
    pygame.draw.line(
        screen,
        "white",
        (len * dir + pos.x, 0 + pos.y),
        (len * dir - arrowsize * dir + pos.x, -arrowsize / 2 + pos.y),
        2,
    )


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

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math

import pygame

# PolarToCartesian
# Convert a polar coordinate (r,theta) to cartesian (x,y):
# x = r * cos(theta)
# y = r * sin(theta)

r = None
theta = 0


def setup():
    global r
    screen = pygame.display.set_mode((640, 360))
    r = screen.get_height() * 0.4
    return screen


def draw(screen: pygame.Surface):
    global r, theta
    screen.fill((255, 255, 255))
    center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    # Convert polar to cartesian
    x = r * math.cos(theta)
    y = r * math.sin(theta)

    # Draw the ellipse at the cartesian coordinate
    pygame.draw.line(screen, "black", center, (x + center.x, y + center.y), 2)
    pygame.draw.aacircle(screen, "gray50", (x + center.x, y + center.y), 24)
    pygame.draw.aacircle(screen, "black", (x + center.x, y + center.y), 24, 1)

    # Increase the angle over time
    theta += 0.01


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

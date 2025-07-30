# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import math

# Recursive Tree
# Renders a simple tree-like structure via recursion
# Branching angle calculated as a function of horizontal mouse position


def setup():
    screen = pygame.display.set_mode((640, 240))
    screen.fill((255, 255, 255))


def draw():
    screen = pygame.display.get_surface()
    assert screen
    screen.fill((255, 255, 255))

    # Mapping the angle between 0 and 90° (HALF_PI) according to mouseX
    mouse_x = pygame.mouse.get_pos()[0]
    angle = math.degrees(map_value(mouse_x, 0, screen.width, 0, math.pi / 2))

    # Start the tree from bottom of the canvas
    branch(80, angle)


# {!1} Each branch now receives its length as an argument
def branch(length, angle, start_point=None, end_point=None):
    screen = pygame.display.get_surface()
    assert screen
    translation = pygame.Vector2(screen.width / 2, screen.height)

    if start_point is None:
        start_point = pygame.Vector2()
    if end_point is None:
        end_point = pygame.Vector2(start_point[0], start_point[1] - length)

    pygame.draw.line(
        screen,
        "black",
        start_point + translation,
        end_point + translation,
        2,
    )

    # {!1} Each branch's length shrinks by two-thirds.
    length *= 0.67

    if length < 2:
        return

    direction = pygame.Vector2(end_point - start_point)
    direction.scale_to_length(length)

    rotate_left = pygame.Vector2(direction).rotate(angle)
    rotate_right = pygame.Vector2(direction).rotate(-angle)

    branch(length, angle, end_point, end_point + rotate_left)
    branch(length, angle, end_point, end_point + rotate_right)


def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    setup()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()
        pygame.display.update()
        clock.tick(60)

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
import math
import random

# Stochastic Tree
# Renders a simple tree-like structure via recursion
# Angles and number of branches are random


def setup(screen):
    screen.fill((255, 255, 255))


def draw(screen):
    screen.fill((255, 255, 255))

    # Start the recursive branching!
    branch(80)


def branch(length, start_point=None, end_point=None):
    screen = pygame.display.get_surface()
    assert screen, "No screen found to draw on!"

    if start_point is None:
        start_point = pygame.Vector2()
    if end_point is None:
        end_point = pygame.Vector2(start_point[0], start_point[1] - length)

    # Start the tree from the bottom of the screen
    translation = pygame.Vector2(screen.width / 2, screen.height)

    # Draw the actual branch
    pygame.draw.aaline(
        screen,
        "black",
        start_point + translation,
        end_point + translation,
        1,
    )  # PygameNote: We use a aaline here (anti-aliased) for better visuals

    # Each branch will be 2/3rds the size of the previous one
    length *= 0.67

    # All recursive functions must have an exite condition!!!
    # Here, ours is when the length of the branch is 2 pixels or less
    if length <= 2:
        return

    # A random number of branches
    n = random.randint(1, 3)
    for _ in range(n):
        new_branch = pygame.Vector2(end_point - start_point)
        new_branch.scale_to_length(length)

        # Pick a random angle
        angle = random.random() * math.pi - (math.pi / 2)
        new_branch.rotate_rad_ip(angle)  # Rotate by theta

        branch(
            length, end_point, end_point + new_branch
        )  # OK, now call myself to branch again


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
        draw(screen)
        pygame.display.update()
        clock.tick(1)

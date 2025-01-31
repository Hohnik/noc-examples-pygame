# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
import random

import pygame


class Mover:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.position = pygame.Vector2(
            random.random() * screen.get_width(), random.random() * screen.get_height()
        )
        self.velocity = pygame.Vector2()
        self.acceleration = pygame.Vector2()
        self.topspeed = 5

    def update(self):
        # Step 1: Compute direction
        self.mouse = pygame.Vector2(pygame.mouse.get_pos())
        dir = self.mouse - self.position

        # Step 2: Normalize
        dir.normalize_ip()

        # Step 3: Scale
        dir *= 0.2

        # Steps 2 and 3 could be combined into:
        # dir.scale_to_length(0.2)

        # Step 4: Accelerate
        self.acceleration = dir

        self.velocity += self.acceleration
        self.velocity = self.velocity.clamp_magnitude(self.topspeed)
        self.position += self.velocity

    def show(self):
        pygame.draw.circle(self.screen, "gray50", self.position, 24)
        pygame.draw.circle(self.screen, "black", self.position, 24, 2)

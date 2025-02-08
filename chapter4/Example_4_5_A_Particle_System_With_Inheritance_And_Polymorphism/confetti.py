# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math

import pygame
from particle import Particle


def map_value(value, in_min, in_max, out_min, out_max):
    return out_min + (value - in_min) * (out_max - out_min) / (in_max - in_min)


class Confetti(Particle):
    def show(self):
        width = self.screen.get_width()
        angle = map_value(self.position.x, 0, width, 0, math.pi * 4)
        angle = math.degrees(angle)

        rect_surf = pygame.Surface((12, 12), pygame.SRCALPHA)
        alpha = int(pygame.math.clamp(self.lifespan, 0, 255))
        pygame.draw.rect(
            rect_surf,
            (127, 127, 127, alpha),
            (0, 0, rect_surf.get_width(), rect_surf.get_height()),
        )
        pygame.draw.rect(
            rect_surf,
            (0, 0, 0, alpha),
            (0, 0, rect_surf.get_width(), rect_surf.get_height()),
            2,
        )

        rect_surf = pygame.transform.rotate(rect_surf, angle)

        rotated_rect = rect_surf.get_rect(center=self.position)

        self.screen.blit(rect_surf, rotated_rect.topleft)

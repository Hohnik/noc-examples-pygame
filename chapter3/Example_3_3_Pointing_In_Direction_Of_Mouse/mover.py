# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math

import pygame


class Mover:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.position = pygame.Vector2(screen.get_width(), screen.get_height())
        self.velocity = pygame.Vector2()
        self.acceleration = 0
        self.topSpeed = 4
        self.xoff = 1000
        self.yoff = 0
        self.r = 16

    def update(self):
        mouse = pygame.Vector2(pygame.mouse.get_pos())
        dir = mouse - self.position
        dir.scale_to_length(0.5)
        self.acceleration = dir

        self.velocity += self.acceleration
        self.velocity = self.velocity.clamp_magnitude(self.topSpeed)
        self.position += self.velocity

    def display(self):
        angle = math.atan2(self.velocity.x, self.velocity.y)
        angle = math.degrees(angle)

        car = pygame.Surface((20, 50), pygame.SRCALPHA)
        car.fill("gray50")
        pygame.draw.rect(car, (0, 0, 0), (0, 0, 20, 50), 2)

        rotated_car = pygame.transform.rotate(car, angle)
        car_rect = rotated_car.get_rect(center=(self.position.x, self.position.y))
        self.screen.blit(rotated_car, car_rect.topleft)

    def checkEdges(self):
        if self.position.x > self.screen.get_width():
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = self.screen.get_width()

        if self.position.y > self.screen.get_height():
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = self.screen.get_height()

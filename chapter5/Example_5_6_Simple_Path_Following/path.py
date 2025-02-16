import pygame


class Path:
    def __init__(self):
        # A path has a radius, i.e how far is it ok for the boid to wander off
        self.screen = pygame.display.get_surface()
        self.radius = 20

        # A path is a line between two points (vectors)
        self.start = pygame.Vector2(0, self.screen.get_height() / 3)
        self.end = pygame.Vector2(
            self.screen.get_width(), 2 / 3 * self.screen.get_height()
        )

    def show(self):
        pygame.draw.line(self.screen, "gray60", self.start, self.end, self.radius * 2)
        pygame.draw.line(self.screen, "black", self.start, self.end)

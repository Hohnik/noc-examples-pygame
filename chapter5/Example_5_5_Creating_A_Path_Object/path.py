import pygame


class Path:
    def __init__(self, screen):
        # A path has a radius, how wide is it.
        # Picking some arbitrary values to initialize the path
        self.screen = screen
        self.radius = 20
        self.start = pygame.Vector2(0, screen.get_height() / 3)
        # A path is only two points, start and end
        self.end = pygame.Vector2(screen.get_width(), 2 / 3 * screen.get_height())

    def show(self):
        pygame.draw.line(self.screen, "gray60", self.start, self.end, self.radius * 2)
        pygame.draw.line(self.screen, "black", self.start, self.end)

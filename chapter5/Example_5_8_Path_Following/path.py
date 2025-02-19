import pygame


class Path:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        # A path has a radius, i.e how far is it ok for the vehicle to wander off
        self.radius = 20
        # A path is now an array of points (Vectors)
        self.points = []

    def addPoint(self, x, y):
        pathPoint = pygame.Vector2(x, y)
        self.points.append(pathPoint)

    def getStart(self):
        return self.points[0]

    def getEnd(self):
        return self.points[-1]

    def show(self):
        # Draw a thicker gray line for the path radius
        pygame.draw.lines(self.screen, "gray60", False, self.points, self.radius * 2)

        # Draw a thin line for the path center
        pygame.draw.lines(self.screen, "black", False, self.points)

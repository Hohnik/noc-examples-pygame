# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from random import gauss

import pygame
from quadtree import Point, QuadTree, Rectangle

# QuadTree
# 1: https://www.youtube.com/watch?v=OJxEcs0w_kE
# 2: https://www.youtube.com/watch?v=QQx_NmCIuCY

# For more:
# https://github.com/CodingTrain/QuadTree

qtree = None


def setup():
    global qtree
    screen = pygame.display.set_mode((640, 360))
    width, height = screen.size

    boundary = Rectangle(width / 2, height / 2, width, height)
    qtree = QuadTree(boundary, 8)

    for i in range(2000):
        x = gauss(width / 2, width / 8)
        y = gauss(height / 2, height / 8)
        p = Point(x, y)
        qtree.insert(p)

    return screen


def draw(screen: pygame.Surface):
    global qtree
    screen.fill((255, 255, 255))
    width, height = screen.size
    mouseX, mouseY = pygame.mouse.get_pos()
    qtree.show()

    area = Rectangle(mouseX, mouseY, 50, 50)

    # This check has been introduced due to a bug discussed in https://github.com/CodingTrain/website/pull/556
    if mouseX < width and mouseY < height:
        surf = pygame.Surface(screen.get_rect().size).convert_alpha()
        surf.fill((0, 0, 0, 0))
        pygame.draw.rect(
            surf,
            (255, 50, 50, 50),
            (area.x - area.w, area.y - area.h, area.w * 2, area.h * 2),
        )
        pygame.draw.rect(
            surf,
            (255, 50, 50),
            (area.x - area.w, area.y - area.h, area.w * 2, area.h * 2),
            2,
        )
        screen.blit(surf)

        points = qtree.query(area)
        for p in points:
            pygame.draw.circle(screen, (50, 50, 50), (p.x, p.y), 2)


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

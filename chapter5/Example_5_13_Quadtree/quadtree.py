# Daniel Shiffman
# http://codingtra.in
# http://patreon.com/codingtrain

import pygame

# QuadTree
# 1: https://www.youtube.com/watch?v=OJxEcs0w_kE
# 2: https://www.youtube.com/watch?v=QQx_NmCIuCY

# For more:
# https://github.com/CodingTrain/QuadTree


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contains(self, point):
        return (
            point.x >= self.x - self.w
            and point.x < self.x + self.w
            and point.y >= self.y - self.h
            and point.y < self.y + self.h
        )

    def intersects(self, area):
        return not (
            area.x - area.w > self.x + self.w
            or area.x + area.w < self.x - self.w
            or area.y - area.h > self.y + self.h
            or area.y + area.h < self.y - self.h
        )


class QuadTree:
    def __init__(self, boundary, n):
        self.screen = pygame.display.get_surface()
        self.boundary = boundary
        self.capacity = n
        self.points = []
        self.divided = False

    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h
        ne = Rectangle(x + w / 2, y - h / 2, w / 2, h / 2)
        self.northeast = QuadTree(ne, self.capacity)
        nw = Rectangle(x - w / 2, y - h / 2, w / 2, h / 2)
        self.northwest = QuadTree(nw, self.capacity)
        se = Rectangle(x + w / 2, y + h / 2, w / 2, h / 2)
        self.southeast = QuadTree(se, self.capacity)
        sw = Rectangle(x - w / 2, y + h / 2, w / 2, h / 2)
        self.southwest = QuadTree(sw, self.capacity)
        self.divided = True

    def insert(self, point):
        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()

            if self.northeast.insert(point):
                return True
            elif self.northwest.insert(point):
                return True
            elif self.southeast.insert(point):
                return True
            elif self.southwest.insert(point):
                return True

    def query(self, area, found=None):
        if found is None:
            found = []

        if not self.boundary.intersects(area):
            return
        else:
            for p in self.points:
                if area.contains(p):
                    found.append(p)

            if self.divided:
                self.northwest.query(area, found)
                self.northeast.query(area, found)
                self.southwest.query(area, found)
                self.southeast.query(area, found)

        return found

    def show(self):
        pygame.draw.rect(
            self.screen,
            "black",
            (
                self.boundary.x - self.boundary.w,
                self.boundary.y - self.boundary.h,
                self.boundary.w * 2,
                self.boundary.h * 2,
            ),
            1,
        )
        for p in self.points:
            pygame.draw.circle(self.screen, "black", (p.x, p.y), 1)

        if self.divided:
            self.northeast.show()
            self.northwest.show()
            self.southeast.show()
            self.southwest.show()

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Re-implementing java.awt.Rectangle (from Processing) for pygame


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def contains(self, px, py):
        return (
            px > self.x
            and px < self.x + self.width
            and py > self.y
            and py < self.y + self.height
        )

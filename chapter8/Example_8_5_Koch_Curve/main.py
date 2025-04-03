# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from koch import KochLine

# Koch Curve
# Renders a simple fractal, the Koch snowflake
# Each recursive level drawn in sequence

# An array for all the line segments
segments = []


def setup():
    screen = pygame.display.set_mode((640, 360))
    screen.fill((255, 255, 255))
    width, height = screen.size

    # Left side of canvas
    start = pygame.Vector2(0, 200)
    # Right side of canvas
    end = pygame.Vector2(width, 200)

    # The first KochLine object
    segments.append(KochLine(start, end))

    # Apply the Koch rules five times.
    for i in range(5):
        generate()

    for segment in segments:
        segment.show()


def generate():
    global segments
    # Create the next array
    next = []
    # For every segment
    for segment in segments:
        # Calculate 5 koch vectors (done for us by the line object)
        a, b, c, d, e = segment.kochPoints()
        # Make line segments between all the vectors and add them
        next.append(KochLine(a, b))
        next.append(KochLine(b, c))
        next.append(KochLine(c, d))
        next.append(KochLine(d, e))

    # The next segments!
    segments = next


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    setup()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        clock.tick(60)

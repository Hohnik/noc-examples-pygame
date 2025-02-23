# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from random import random

import pygame
from boid import Boid
from flock import Flock

# Demonstration of Craig Reynolds' "Flocking" behavior
# See: http://www.red3d.com/cwr/
# Rules: Cohesion, Separation, Alignment

# Click mouse to add boids into the system

flock = None

# bin-lattice spatial subdivision
grid = None
cols = None
rows = None
resolution = 40  # adjust as necessary


def make2DArray(cols, rows):
    return [[[] for _ in range(cols)] for _ in range(rows)]


def setup():
    global flock, grid, cols, rows, resolution
    screen = pygame.display.set_mode((640, 360))

    width, height = screen.size
    cols = width // resolution
    rows = height // resolution
    grid = make2DArray(cols, rows)
    flock = Flock()

    # Add an initial set of boids into the system
    for i in range(120):
        boid = Boid(random() * width, random() * height)
        flock.addBoid(boid)
    return screen


def draw(screen: pygame.Surface):
    global flock, grid, cols, rows, resolution
    screen.fill((255, 255, 255))
    width, height = screen.size

    # Reset grid at the beginning of each frame
    for i in range(cols):
        for j in range(rows):
            grid[j][i] = []

    # Place each boid into the appropriate cell in the grid
    for boid in flock.boids:
        col = int(boid.position.x // resolution)
        row = int(boid.position.y // resolution)
        col = max(0, min(col, col - 1))
        row = max(0, min(row, row - 1))
        grid[row][col].append(boid)

    # Draw the grid
    # Draw vertical lines
    for i in range(cols + 1):
        x = i * resolution
        pygame.draw.line(screen, "gray70", (x, 0), (x, height))

    # Draw horizontal lines
    for j in range(rows + 1):
        y = j * resolution
        pygame.draw.line(screen, "gray70", (0, y), (width, y))

    # Hilight the 3x3 neighborhood the mouse is over
    mouseX, mouseY = pygame.mouse.get_pos()
    mouseCol = mouseX // resolution
    mouseRow = mouseY // resolution

    for i in range(-1, 2):
        for j in range(-1, 2):
            col = mouseCol + i
            row = mouseRow + j

            # Check if the cell is within the grid
            if col >= 0 and col < cols and row >= 0 and row < rows:
                surf = pygame.Surface(screen.get_rect().size).convert_alpha()
                surf.fill((0, 0, 0, 0))
                pygame.draw.rect(
                    surf,
                    (255, 50, 50, 100),
                    (col * resolution, row * resolution, resolution, resolution),
                )
                screen.blit(surf)

    flock.run(grid, cols, rows, resolution)

    # Add a new boid into the System
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        flock.addBoid(Boid(mouseX, mouseY))


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

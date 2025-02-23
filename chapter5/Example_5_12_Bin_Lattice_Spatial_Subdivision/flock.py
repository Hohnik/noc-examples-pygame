# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Flock object
# Does very little, simply manages the array of all the boids


class Flock:
    def __init__(self):
        # An array for all the boids
        self.boids = []  # Initialize the array

    def run(self, grid, cols, rows, resolution):
        for boid in self.boids:
            boid.run(grid, cols, rows, resolution)

    def addBoid(self, boid):
        self.boids.append(boid)

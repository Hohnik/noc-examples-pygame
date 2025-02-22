# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Flock object
# Does very little, simply manages the array of all the boids


class Flock:
    def __init__(self):
        # An array for all the boids
        self.boids = []  # Initialize the array

    def run(self):
        for boid in self.boids:
            boid.run(
                self.boids
            )  # Passing the entire list of boids to each boid individually

    def addBoid(self, b):
        self.boids.append(b)

import pygame
from configs import target

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Pathfinding w/ Genetic Algorithms

# Rocket class -- this is just like our Boid / Particle class
# the only difference is that it has DNA & fitness


class Rocket:
    def __init__(self, x, y, dna):
        self.screen = pygame.display.get_surface()

        # All of our physics stuff
        self.acceleration = pygame.Vector2()
        self.velocity = pygame.Vector2()
        self.position = pygame.Vector2(x, y)

        # Size
        self.r = 4

        # Fitness and DNA
        self.fitness = 0
        self.dna = dna

        # To count which force we're on in the genes
        self.geneCounter = 0

    # Fitness function
    # fitness = one devided by distance squared
    def calculateFitness(self):
        distance = pygame.Vector2.distance_to(self.position, target)
        self.fitness = 1 / (distance * distance)

    # Run in relation to all the obstacles
    # If I'm stuck, don't bother updating or checking for intersections
    def run(self):
        self.applyForce(self.dna.genes[self.geneCounter])
        self.geneCounter += 1
        self.update()
        self.show()

    def applyForce(self, force):
        self.acceleration += force

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

    def show(self):
        assert self.screen, "No pygame display surface found."

        # Draw a triangle rotated in the direction of velocity
        angle = self.velocity.as_polar()[1]

        head = pygame.Vector2(self.r * 2, 0).rotate(angle)
        back_left = pygame.Vector2(-self.r * 2, -self.r).rotate(angle)
        back_right = pygame.Vector2(-self.r * 2, self.r).rotate(angle)

        offset = self.position  # Translation
        pygame.draw.polygon(
            self.screen,
            "gray",
            [head + offset, back_left + offset, back_right + offset],
        )
        pygame.draw.polygon(
            self.screen,
            "black",
            [head + offset, back_left + offset, back_right + offset],
            1,
        )

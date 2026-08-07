import pygame

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

        self.finishCounter = (
            0  # We're going to count how long it takes to reach the target
        )
        self.recordDistance = float(
            "inf"
        )  # Some high number that will be beat instantly
        self.hitObstacle = False  # Am I stuck on an obstacle?
        self.hitTarget = False  # Did I reach the target?

    # FITNESS FUNCTION
    # distance = distance from target
    # finish = what order did i finish (first, second, etc ...)
    # f(distance, finish) = (1.0f / finish**1.5) * (1.0f / distance**6)
    # a lower finish is rewarded (exponantially) and/or shorter distance to target (exponentially)
    def calculateFitness(self):
        # Reward finishing faster and getting close
        self.fitness = 1 / (self.finishCounter * self.recordDistance)

        # Let's try to do the 4th power!
        self.fitness = pow(self.fitness, 4)

        # Lose 90% of fitness hitting an obstacle
        if self.hitObstacle:
            self.fitness *= 0.1

        # Double the fitness for finishing!
        if self.hitTarget:
            self.fitness *= 2

    # Run in relation to all the obstacles
    # If I'm stuck, don't bother updating or checking for intersections
    def run(self, obstacles):
        # Stop the rocket if it's hit an obstacle or the target
        if self.hitObstacle or self.hitTarget:
            self.show()
            return

        self.applyForce(self.dna.genes[self.geneCounter])
        self.geneCounter += 1
        self.update()
        self.checkObstacles(obstacles)  # Check if rocket hit an obstacle
        self.show()

    def checkTarget(self, target):
        distance = pygame.Vector2.distance_to(self.position, target.position)

        # Check if the distance is closer than the "record" distance.
        # If it is, set a new record.
        self.recordDistance = min(self.recordDistance, distance)

        # If the object reaches the target, set a boolean flag to true.
        if target.contains(self.position):
            self.hitTarget = True

        # Increase the finish counter if it hasn't hit the target
        if not self.hitTarget:
            self.finishCounter += 1

    # This new function lives in the Rocket class and checks
    # if a rocket has hit an obstacle.
    def checkObstacles(self, obstacles):
        for obstacle in obstacles:
            if obstacle.contains(self.position):
                self.hitObstacle = True

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

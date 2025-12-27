# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import random
import pygame
from rocket import Rocket
from dna import DNA

# Pathfinding w/ Genetic Algorithms

# A class to describe a population of "creatures"


# Initialize the population
class Population:
    def __init__(self, mutation, length):
        self.screen = pygame.display.get_surface()
        assert self.screen, "Created Population before initializing Pygame display"

        self.mutationRate = mutation  # Mutation rate
        self.population: list[Rocket] = []  # Array to hold the current population
        self.matingPool = []  # ArrayList which we will use for our "mating pool"
        self.generations = 0  # Number of generations

        # make a new set of creatures
        for _ in range(length):
            x = self.screen.get_width() / 2
            y = self.screen.get_height() - 5
            self.population.append(Rocket(x, y, DNA()))

    def live(self):
        for rocket in self.population:
            # The run method takes care of the simulation, updates the rockt's
            # position and draw it to the canvas.
            rocket.run()

    # Calculate the fitness for each rocket.
    def fitness(self):
        for rocket in self.population:
            rocket.calculateFitness()

    # The selection method normalizes all the fitness values.
    def selection(self):
        # Sum all of the fitness values.
        totalFitness = 0
        for rocket in self.population:
            totalFitness += rocket.fitness

        # Divide by the total to normalize the fitness values.
        for rocket in self.population:
            rocket.fitness /= totalFitness

    # Making the next generation
    def reproduction(self):
        # Create a new population with children from the mating pool
        nextPopulation: list[Rocket] = []
        for i in range(len(self.population)):
            # Spin the wheel of fortune to pick two parents dnas
            parentA = self.weightedSelection()
            parentB = self.weightedSelection()
            child = parentA.crossover(parentB)

            # Mutate their genes
            child.mutate(self.mutationRate)
            assert self.screen
            x = self.screen.get_width() / 2
            y = self.screen.get_height() - 5
            nextPopulation.append(Rocket(x, y, child))

        # Replace the old population
        self.population = nextPopulation
        self.generations += 1

    def weightedSelection(self) -> DNA:
        # Start with the first element
        index = 0

        # Pick a starting point
        start = random.random()

        # At the finish line?
        while start > 0:
            # Move a distance according to fitness
            start -= self.population[index].fitness
            # Next element
            index += 1

        # Undo moving to the next element since the finish has been reached
        index -= 1
        return self.population[index].dna

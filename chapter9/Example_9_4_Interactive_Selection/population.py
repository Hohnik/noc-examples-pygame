# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import random

import pygame
from dna import DNA
from flower import Flower

# Pathfinding w/ Genetic Algorithms

# A class to describe a population of faces
# this hasn't changed very much from example to example


# Create the population
class Population:
    def __init__(self, mutationRate, size):
        self.screen = pygame.display.get_surface()
        assert self.screen, "Initialize pygame display before creating population"

        self.mutationRate = mutationRate  # Mutation rate
        self.flowers = []  # Array to hold the current population
        self.matingPool = []
        self.generations = 0  # Number of generations

        # Make a new set of creatures
        for i in range(size):
            self.flowers.append(Flower(DNA(), 10 + i * 79, 60))

    # Display all faces
    def show(self):
        for flower in self.flowers:
            flower.show()

    # Are we rolling over any of the faces?
    def rollover(self, mx, my):
        for flower in self.flowers:
            flower.rollover(mx, my)

    def weightedSelection(self):
        # Start with the first element
        index = 0

        # Pick a starting point
        start = random.random()

        # At the finish line?
        while start > 0:
            # Move a distance according to fitness
            start = start - self.flowers[index].fitness
            # Next element
            index += 1

        # Undo moving to the next element since the finish has been reached
        index -= 1
        return self.flowers[index]

    # The selection method normalizes all the fitness values.
    def selection(self):
        # Sum all of the fitness values.
        totalFitness = 0
        for flower in self.flowers:
            totalFitness += flower.fitness

        # Divide by the total to normalize the fitness values.
        for flower in self.flowers:
            flower.fitness /= totalFitness

    # Making the next generation
    def reproduction(self):
        # Create a new population with children from the mating pool
        nextFlowers = []
        for i in range(len(self.flowers)):
            # Spin the wheel of fortune to pick two parents
            parentA = self.weightedSelection()
            parentB = self.weightedSelection()
            child = parentA.dna.crossover(parentB.dna)

            # Mutate their genes
            child.mutate(self.mutationRate)
            nextFlowers.append(Flower(child, 10 + i * 79, 60))

        # Replace the old population
        self.flowers = nextFlowers
        self.generations += 1

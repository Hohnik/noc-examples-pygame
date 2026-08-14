# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Evolution EcoSystem

from random import random

import pygame
from bloop import Bloop
from dna import DNA
from food import Food

# The World we live in
# Has bloops and food


class World:
    # The World class manages the population of bloops and all the food

    def __init__(self, populationSize):
        self.screen = pygame.display.get_surface()
        assert self.screen, "No pygame display surface found."

        # Create the population
        self.bloops = []
        for _ in range(populationSize):
            position = pygame.Vector2(
                random() * self.screen.get_width(),
                random() * self.screen.get_height(),
            )
            dna = DNA()
            self.bloops.append(Bloop(position, dna))

        # Create the food
        self.food = Food(populationSize)

    # Run the world
    def run(self):
        # This function draws the food and adds new food when necessary
        self.food.run()

        # Manage the bloops (cycle through array backwards since bloops are deleted.)
        for i in range(len(self.bloops) - 1, -1, -1):
            # All bloops run and eat
            bloop = self.bloops[i]
            bloop.run()
            bloop.eat(self.food)

            # If it's dead, remove it and create food
            if bloop.dead():
                self.bloops.pop(i)
                self.food.add(bloop.position)

            # Here is were each living bloop has a chance to reproduce
            # If it does, it is added to the population.
            # Note the value of "child" is undefined if it does not.
            else:
                child = bloop.reproduce()
                if child:
                    self.bloops.append(child)

    def born(self, x, y):
        position = pygame.Vector2(x, y)
        dna = DNA()
        self.bloops.append(Bloop(position, dna))

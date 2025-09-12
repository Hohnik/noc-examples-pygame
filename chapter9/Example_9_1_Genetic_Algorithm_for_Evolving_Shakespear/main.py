# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from random import choice
from DNA import DNA
from utils import wrap_text, render_text_list

# Genetic Algorithm, Evolving Shakespeare

# Demonstration of using a genetic algorithm to perform a search

# setup()
#  # Step 1: The Population
#    # Create an empty population (an array or ArrayList)
#    # Fill it with DNA encoded objects (pick random values to start)

# draw()
#  # Step 1: Selection
#    # Create an empty mating pool (an empty ArrayList)
#    # For every member of the population, evaluate its fitness based on some criteria / function,
#      and add it to the mating pool in a manner consistant with its fitness, i.e. the more fit it
#      is the more times it appears in the mating pool, in order to be more likely picked for reproduction.

#  # Step 2: Reproduction Create a new empty population
#    # Fill the new population by executing the following steps:
#       1. Pick two "parent" objects from the mating pool.
#       2. Crossover -- create a "child" object by mating these two parents.
#       3. Mutation -- mutate the child's DNA based on a given probability.
#       4. Add the child object to the new population.
#    # Replace the old population with the new population
#
#   # Rinse and repeat


# Mutation rate
mutationRate = 0.01
# Population Size
populationSize = 150

# Population array
population = []

# Target phrase
target = "to be or not to be"


def setup():
    # Step 1: Initialize Population
    for _ in range(populationSize):
        population.append(DNA(len(target)))


def draw(screen: pygame.Surface):
    # Step 2: Selection
    # Step 2a: Calculate fitness.
    for phrase in population:
        phrase.calculateFitness(target)

    # Step 2b: Build mating pool.
    matingPool = []

    for phrase in population:
        # Add each member n times according to its fitness score.
        n = int((phrase.fitness * 100) // 1)
        for _ in range(n):
            matingPool.append(phrase)

    # Step 3: Reproduction
    for i in range(len(population)):
        partnerA = choice(matingPool)
        partnerB = choice(matingPool)
        # Step 3a: Crossover
        child = partnerA.crossover(partnerB)
        # Step 3b: Mutation
        child.mutate(mutationRate)

        # Note that we are overwriting the population with the new
        # children.  When draw() loops, we will perform all the same
        # steps with the new population of children.
        population[i] = child

    everything = ""
    for i in range(len(population)):
        everything += population[i].getPhrase() + "    "

    screen.fill((255, 255, 255))

    font = pygame.font.SysFont("courier", 12)
    wrapped_text = wrap_text(everything, font, screen.get_width() - 24)
    print(wrapped_text)
    text = render_text_list(wrapped_text, font, "black")
    screen.blit(text, (12, 0))


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 240))
    setup()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw(screen)
        pygame.display.update()
        clock.tick(60)

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import random

# Genetic Algorithm, Evolving Shakespeare

# A class to describe a psuedo-DNA, i.e. genotype
#   Here, a virtual organism's DNA is an array of character.
#   Functionality:
#      -- convert DNA into a string
#      -- calculate DNA's "fitness"
#      -- mate DNA with another set of DNA
#      -- mutate DNA

# Return a random character (letter, number, symbol, space, etc)


def randomCharacter():
    c = random.randint(32, 126) // 1
    return chr(c)


# Constructor (makes a random DNA)
class DNA:
    # Create DNA randomly.
    def __init__(self, length):
        self.genes = []
        # Adding a variable to track fitness.
        self.fitness = 0
        for _ in range(length):
            self.genes.append(randomCharacter())

    # Converts array to String—PHENOTYPE.
    def getPhrase(self):
        return "".join(self.genes)

    # Calculate fitness.
    def calculateFitness(self, target):
        score = 0
        for i in range(len(self.genes)):
            if self.genes[i] == target[i]:
                score += 1
        self.fitness = score / len(target)

    # Crossover
    def crossover(self, partner):
        # The child is a new instance of DNA.
        # (Note that the genes are generated randomly in DNA constructor,
        # but the crossover function will override the array.)
        child = DNA(len(self.genes))

        # Picking a random “midpoint” in the genes array
        midpoint = random.randint(0, len(self.genes) - 1)

        for i in range(len(self.genes)):
            # Before the midpoint genes from self DNA
            if i < midpoint:
                child.genes[i] = self.genes[i]
            # After the midpoint from the partner DNA
            else:
                child.genes[i] = partner.genes[i]
        return child

    # Mutation
    def mutate(self, mutationRate):
        # Looking at each gene in the array
        for i in range(len(self.genes)):
            # Check a random number against mutation rate
            if random.random() < mutationRate:
                # Mutation, a new random character
                self.genes[i] = randomCharacter()

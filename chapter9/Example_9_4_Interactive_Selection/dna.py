# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from __future__ import annotations

import math
import random


class DNA:
    def __init__(self):
        # DNA is random floating point values between 0 and 1
        # The genetic sequence
        self.genes = [random.random() for _ in range(14)]

    def crossover(self, partner: DNA):
        child = DNA()

        # Picking a random “midpoint” in the genes array
        midpoint = math.floor(random.random() * len(self.genes))

        # Before the midpoint genes from self DNA
        # After the midpoint from the partner DNA
        child.genes = self.genes[:midpoint] + partner.genes[midpoint:]

        return child

    # Mutation
    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                self.genes[i] = random.random()

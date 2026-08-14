# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

from __future__ import annotations

from random import random


class DNA:
    def __init__(self):
        # The genetic sequence
        # DNA is random floating point values between 0 and 1
        self.genes = [random() for _ in range(1)]

    def copy(self):
        # It gets made with random DNA
        newDNA = DNA()

        # But then it is overwritten
        newDNA.genes = self.genes[::]
        return newDNA

    # Based on a mutation probability, pick a new random character in array spots
    def mutate(self, mutationRate):
        for i in range(len(self.genes)):
            if random() < mutationRate:
                self.genes[i] = random()

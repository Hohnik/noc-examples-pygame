from __future__ import annotations

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

import random
import math

from configs import lifeSpan


# DNA is an array of vectors
class DNA:
    def __init__(self):
        # The genetic sequence
        self.genes: list[pygame.Vector2] = []
        # The maximum strength of the forces
        self.maxforce = 0.1
        for _ in range(lifeSpan):
            angle = random.random() * math.pi * 2
            magnitude = random.random() * self.maxforce

            gene = pygame.Vector2(1, 0)
            gene.scale_to_length(magnitude)
            gene.rotate_rad_ip(angle)

            self.genes.append(gene)

    # Crossover
    # Creates new DNA sequence from two (self & partner)
    def crossover(self, partner: DNA):
        # The child is a new instance of DNA.
        # (Note that the genes are generated randomly in DNA constructor,
        # but the crossover function will override the array.)
        child = DNA()

        # Picking a random “midpoint” in the genes array
        midpoint = math.floor(random.random() * len(self.genes))

        # Before the midpoint genes from self DNA
        # After the midpoint from the partner DNA
        child.genes = self.genes[midpoint:] + partner.genes[:midpoint]

        return child

    # Mutation
    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                angle = random.random() * math.pi * 2
                magnitude = random.random() * self.maxforce

                self.genes[i] = pygame.Vector2(1, 0)
                self.genes[i].scale_to_length(magnitude)
                self.genes[i].rotate_rad_ip(angle)

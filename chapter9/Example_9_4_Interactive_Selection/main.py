# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from population import Population
from utils import Button, Text

# Interactive Selection
# http://www.genarts.com/karl/papers/siggraph91.html

populationSize = 8  # This is a very small population!
mutationRate = 0.05  # A pretty high mutation rate here, out population is rather small we need to enforce variety


def setup(screen: pygame.Surface):
    global population, button, text
    # Create the population
    population = Population(mutationRate, populationSize)

    # Custom button implementation in utils.py
    font = pygame.font.SysFont("courier", 12)
    button = Button(10, 10, font, "evolve new generation", onclick=nextGeneration)
    text = Text(12, screen.get_height() - 20, font, "Generation #0")


def draw(screen: pygame.Surface):
    screen.fill("white")

    for event in pygame.event.get():
        button.handle_event(event)
    button.draw(screen)

    # Draw the flowert
    population.show()

    # Check for increasing fitness
    population.rollover(*pygame.mouse.get_pos())

    text.set_text(f"Generation #{population.generations}")
    text.draw(screen)


def nextGeneration():
    population.weightedSelection()
    population.reproduction()


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 240))
    setup(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw(screen)
        pygame.display.update()
        clock.tick(60)

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from utils import render_text_list
from population import Population
from configs import mutationRate, lifeSpan, lifeCounter, target

# Smart Rockets w/ Genetic Algorithms

# Each Rocket's DNA is an array of p5.Vectors
# Each p5.Vector acts as a force for each frame of animation
# Imagine a booster on the end of the rocket that can point in any direction
# and fire at any strength every frame

# The Rocket's fitness is a function of how close it gets to the target as well as how fast it gets there

# This example is inspired by Jer Thorp's Smart Rockets
# http://www.blprnt.com/smartrockets/


# Create a population with a mutation rate, and population max
population = None


def setup(screen: pygame.Surface):
    global population
    target.update(screen.get_width() / 2, 24)
    population = Population(mutationRate, 50)  # Population


def draw(screen: pygame.Surface):
    global lifeCounter, lifeSpan, population
    screen.fill("white")

    # Draw the start and target positions
    pygame.draw.aacircle(screen, "gray", (int(target.x), int(target.y)), 12)
    pygame.draw.aacircle(screen, "black", (int(target.x), int(target.y)), 12, 1)

    assert population is not None, "Population not initialized"
    if lifeCounter < lifeSpan:  # If the generation hasn't ended yet
        population.live()
        lifeCounter += 1
    else:  # Otherwise a new generation
        lifeCounter = 0
        population.fitness()
        population.selection()
        population.reproduction()

    # Display some info
    font = pygame.font.SysFont("courier", 12)
    text = render_text_list(
        [
            f"Generation #: {population.generations}",
            f"Cycles left: {lifeSpan - lifeCounter}",
        ],
        font,
        "black",
    )
    screen.blit(text, (10, 10))

    # Move the target if the mouse is pressed
    # System will adapt to new target
    if pygame.mouse.get_just_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        target.update(x, y)


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

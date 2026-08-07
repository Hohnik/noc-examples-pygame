# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from configs import lifeCounter, lifeSpan, mutationRate, recordTime
from obstacle import Obstacle
from population import Population
from utils import render_text_list

# Smart Rockets w/ Genetic Algorithms

# Each Rocket's DNA is an array of Vectors
# Each Vector acts as a force for each frame of animation
# Imagine a booster on the end of the rocket that can point in any direction
# and fire at any strength every frame

# The Rocket's fitness is a function of how close it gets to the target as well as how fast it gets there

# This example is inspired by Jer Thorp's Smart Rockets
# http://www.blprnt.com/smartrockets/


def setup(screen: pygame.Surface):
    global population, target, obstacles
    population = Population(mutationRate, 150)  # Population

    target = Obstacle(screen.get_width() / 2 - 12, 24, 24, 24)
    obstacles = []
    obstacles.append(
        Obstacle(screen.get_width() / 2 - 75, screen.get_height() / 2, 150, 10)
    )


def draw(screen: pygame.Surface):
    global lifeCounter, recordTime
    screen.fill("white")

    # Draw the start and target positions
    target.show()

    assert population is not None, "Population not initialized"
    if lifeCounter < lifeSpan:  # If the generation hasn't ended yet
        population.live(obstacles, target)
        if population.targetReached() and lifeCounter < recordTime:
            recordTime = lifeCounter
        else:
            lifeCounter += 1
    else:  # Otherwise a new generation
        lifeCounter = 0
        population.calculateFitness()
        population.selection()
        population.reproduction()

    # Draw the obstacles
    for obstacle in obstacles:
        obstacle.show()

    # Display some info
    font = pygame.font.SysFont("courier", 12)
    text = render_text_list(
        [
            f"Generation #: {population.generations}",
            f"Cycles left: {lifeSpan - lifeCounter}",
            f"Record cycles: {recordTime}",
        ],
        font,
        "black",
    )
    screen.blit(text, (10, 10))

    # Move the target if the mouse is pressed
    # System will adapt to new target
    if pygame.mouse.get_just_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        target.position.x = x
        target.position.y = y
        recordTime = lifeSpan


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

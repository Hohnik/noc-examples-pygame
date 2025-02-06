# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from bob import Bob
from spring import Spring

running = True

# Mover object
bob = None

# Spring object
spring = None


def setup():
    global bob, spring
    screen = pygame.display.set_mode((640, 360))
    # Create objects at starting position
    # Note third argument in Spring constructor is "rest length"
    spring = Spring(screen, screen.width / 2, 10, 100)
    bob = Bob(screen, screen.width / 2, 100)
    return screen


def draw(screen: pygame.Surface):
    global bob, spring, running
    screen.fill("white")

    # Apply a gravity force to the bob
    gravity = pygame.Vector2(0, 2)
    bob.applyForce(gravity)

    # Update bob
    bob.update()
    bob.handleDrag(*pygame.mouse.get_pos())

    # Connect the bob to the spring (this calculates the force)
    spring.connect(bob)

    # Constrain spring distance between min and max
    spring.constrainLength(bob, 30, 200)

    # Draw everything
    spring.showLine(bob)  # Draw a line between spring and bob
    bob.show()
    spring.show()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bob.handleClick(*pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:
            bob.stopDragging()


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    screen = setup()

    while running:
        draw(screen)

        pygame.display.flip()
        clock.tick(60)

# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

# Example 1-1: Bouncing Ball, no vectors
# Variables for position and speed of ball.
x = 100
y = 100
xspeed = 2.5
yspeed = 2


def setup():
    screen = pygame.display.set_mode((640, 360))
    return screen


def draw(screen):
    global x, y, yspeed, xspeed
    screen.fill((255, 255, 255))

    # Move the ball according to its speed.
    x += xspeed
    y += yspeed

    # {!6} Check for bouncing.
    if x > screen.get_width() or x < 0:
        xspeed = xspeed * -1
    if y > screen.get_height() or y < 0:
        yspeed = yspeed * -1

    # {!1} Draw the ball at the position (x,y).
    pygame.draw.circle(screen, (127, 127, 127), (x, y), 24)  # ball
    pygame.draw.circle(screen, "black", (x, y), 24, 1)  # border


if __name__ == "__main__":
    pygame.init()
    screen = setup()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw(screen)

        pygame.display.flip()
        clock.tick(60)

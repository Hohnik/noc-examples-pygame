# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

# Example 1-2: Bouncing Ball, with p5.Vector!
# {!2 .bold} Instead of a bunch of floats, we now just have two variables.
position = None
velocity = None


def setup():
    global position, velocity
    screen = pygame.display.set_mode((640, 360))
    # {!2 .bold} Note how pygame.Vector2() has to be called inside of setup().
    position = pygame.Vector2(100, 100)
    velocity = pygame.Vector2(2.5, 2)
    return screen


def draw(screen):
    global position, velocity
    screen.fill((255, 255, 255))

    # {!1 .bold .no-comment}
    position += velocity

    # {!6 .bold .code-wide} We still sometimes need to refer to the individual components of a pygame.Vector and can do so using the dot syntax: position.x, velocity.y, etc.
    if position.x > screen.get_width() or position.x < 0:
        velocity.x = velocity.x * -1

    if position.y > screen.get_height() or position.y < 0:
        velocity.y = velocity.y * -1

    pygame.draw.circle(screen, (127, 127, 127), (position.x, position.y), 24)  # ball
    pygame.draw.circle(screen, "black", (position.x, position.y), 24, 1)  # border


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

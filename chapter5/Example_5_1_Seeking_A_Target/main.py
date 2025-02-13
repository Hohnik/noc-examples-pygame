# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame
from vehicle import Vehicle

# Seeking "vehicle" follows the mouse position

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

vehicle = None


def setup():
    global vehicle
    screen = pygame.display.set_mode((640, 360))
    vehicle = Vehicle(screen, screen.get_width() / 2, screen.get_height() / 2)
    return screen


def draw(screen: pygame.Surface):
    screen.fill((255, 255, 255))

    mouse = pygame.Vector2(pygame.mouse.get_pos())

    # Draw an ellipse at the mouse position
    pygame.draw.circle(screen, "gray50", mouse, 24)
    pygame.draw.circle(screen, "black", mouse, 24, 2)

    # Call the appropriate steering behaviors for our agents
    vehicle.seek(mouse)
    vehicle.update()
    vehicle.show()


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = setup()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw(screen)
        pygame.display.flip()
        clock.tick(60)

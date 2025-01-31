# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com


import noise  # external library > `pip install noise`
import pygame

walker = None


def setup():
    global walker
    screen = pygame.display.set_mode((640, 360))  # creating canvas of size 640 x 360
    walker = Walker(screen)  # creating an instance/object of class Walker
    screen.fill((255, 255, 255))


def draw(screen):
    global walker
    walker.step()
    walker.show()


class Walker:
    def __init__(self, screen):
        self.screen = screen
        self.tx = 0
        self.ty = 1000

    def show(self):
        pygame.draw.circle(self.screen, (127, 127, 127), (self.x, self.y), 24)
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x, self.y), 24, 1)

    def step(self):
        # {!2} x- and y-position mapped from noise
        self.x = remap(noise.pnoise1(self.tx), -1, 1, 0, self.screen.get_width())
        self.y = remap(noise.pnoise1(self.ty), -1, 1, 0, self.screen.get_height())

        # {!2} Move forward through “time.”
        self.tx += 0.01
        self.ty += 0.01


def remap(value, min_val, max_val, target_min=0, target_max=1):
    return target_min + (value - min_val) * (target_max - target_min) / (
        max_val - min_val
    )


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
        clock.tick(120)

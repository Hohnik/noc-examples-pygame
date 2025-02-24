# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

# Array of cells
cells = None
# Starting at generation 0
generation = 0
# Cell size
w = 10

# Rule 90
ruleset = [0, 1, 0, 1, 1, 0, 1, 0]

# # Rule 77
# ruleset = [0, 1, 0, 0, 1, 1, 0, 1]

# # Rule 105
# ruleset = [0, 1, 1, 0, 1, 0, 0, 1]


def setup():
    global cells
    screen = pygame.display.set_mode((640, 360))
    screen.fill((255, 255, 255))

    # An Array of 0s and 1s
    cells = [0 for _ in range(int(screen.get_width() // w))]
    cells[int(len(cells) // 2)] = 1


def draw():
    global running, cells, generation
    screen = pygame.display.get_surface()

    for i in range(1, len(cells) - 1):
        # Only drawing the cell's with a state of 1
        if cells[i] == 1:
            pygame.draw.rect(screen, "black", (i * w, generation * w, w, w))

    nextgen = cells[:]
    for i in range(1, len(cells) - 1):
        left = cells[i - 1]
        me = cells[i]
        right = cells[i + 1]
        nextgen[i] = rules(left, me, right)
    cells = nextgen

    # The next generation
    generation += 1


# Look up a new state from the ruleset
def rules(a, b, c):
    s = f"{a}{b}{c}"
    index = int(s, 2)
    return ruleset[7 - index]


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    setup()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()
        pygame.display.update()
        clock.tick(60)

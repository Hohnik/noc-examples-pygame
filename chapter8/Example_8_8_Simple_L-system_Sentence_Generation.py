# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame


def setup(screen):
    screen.fill("white")

    # {!1} Start with an axiom.
    current = "A"

    # 9 generations
    for i in range(9):
        current = generate(current)

        # Render text to canvas
        font = pygame.font.SysFont("courier", 16)
        text = font.render(f"{i}: {current}", True, "black")
        screen.blit(text, (4, 8 + i * 16))


def generate(current_text):
    next = ""

    # For every character of the current sentence
    for c in current_text:
        # Apply the product rules A->AB, B->A
        if c == "A":
            next += "AB"
        elif c == "B":
            next += "A"

    return next


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 160))
    setup(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

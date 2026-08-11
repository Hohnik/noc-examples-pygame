from typing import ClassVar

import pygame


def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class Text:
    def __init__(self, x, y, font, text="", colour=(0, 0, 0), anchor="topleft"):
        self.font = font
        self.colour = colour
        self.anchor = anchor
        self.pos = (x, y)
        self.set_text(text)

    def set_text(self, text):
        self.text = text
        self.surface = self.font.render(text, True, self.colour)
        self.rect = self.surface.get_rect(**{self.anchor: self.pos})

    def draw(self, screen):
        screen.blit(self.surface, self.rect)


class Button:
    COLORS: ClassVar = {"normal": "#dddddd", "hover": "#666666", "pressed": "#333333"}

    def __init__(self, x, y, font, text="Button", onclick=None, padding=(9, 7)):
        self.onclick = onclick
        self.held = False
        self.text_surf = font.render(text, True, (20, 20, 20))
        w, h = self.text_surf.get_size()
        self.rect = pygame.Rect(x, y, w + padding[0] * 2, h + padding[1] * 2)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def handle_event(self, event):
        hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and hovered:
            self.held = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.held and hovered and self.onclick:
                self.onclick()
            self.held = False

    def draw(self, screen):
        hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        state = "pressed" if self.held and hovered else "hover" if hovered else "normal"
        pygame.draw.rect(screen, self.COLORS[state], self.rect)
        pygame.draw.rect(screen, "black", self.rect, 1)
        screen.blit(self.text_surf, self.text_rect)

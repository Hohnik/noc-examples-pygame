import pygame

# Bob object, just like our regular Mover (location, velocity, acceleration, mass)


class Bob:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2()
        self.acceleration = pygame.Vector2()
        self.mass = 24
        # Arbitrary damping to simulate friction / drag
        self.damping = 0.98
        # For user interaction
        self.dragOffset = pygame.Vector2()
        self.dragging = False

    # Standard Euler integration
    def update(self):
        self.velocity += self.acceleration
        self.velocity *= self.damping
        self.position += self.velocity
        self.acceleration *= 0

    # Newton's law: F = M * A
    def applyForce(self, force: pygame.Vector2):
        f = force.copy()
        f /= self.mass
        self.acceleration += f

    # Draw the bob
    def show(self):
        color = "gray50"
        if self.dragging:
            color = "gray80"

        pygame.draw.circle(self.screen, color, self.position, self.mass)
        pygame.draw.circle(self.screen, "black", self.position, self.mass, 2)

    def handleClick(self, mx, my):
        d = self.position.distance_to((mx, my))
        if d < self.mass:
            self.dragging = True
            self.dragOffset.x = self.position.x - mx
            self.dragOffset.y = self.position.y - my

    def stopDragging(self):
        self.dragging = False

    def handleDrag(self, mx, my):
        if self.dragging:
            self.position.x = mx + self.dragOffset.x
            self.position.y = my + self.dragOffset.y

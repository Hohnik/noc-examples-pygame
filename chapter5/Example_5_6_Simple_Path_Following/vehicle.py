# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

# The "Vehicle" class


class Vehicle:
    def __init__(self, x, y, maxspeed, maxforce):
        self.screen = pygame.display.get_surface()
        self.position = pygame.Vector2(x, y)
        self.acceleration = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(2, 0)
        self.r = 4
        self.maxspeed = maxspeed
        self.maxforce = maxforce
        self.debug = True

    def run(self):
        self.update()
        self.show()

    # This function implements Craig Reynolds' path following algorithm
    # http://www.red3d.com/cwr/steer/PathFollow.html
    def follow(self, path):
        # Step 1: Predict the vehicle’s future position.
        future = self.velocity.copy()
        future.scale_to_length(25)
        future += self.position

        # Step 2: Find the normal point along the path.
        normalPoint = getNormalPoint(future, path.start, path.end)

        # Step 3: Move a little further along the path and set a target.
        b = path.end - path.start
        b.scale_to_length(25)
        target = normalPoint + b

        # Step 4: If we are off the path,
        # seek that target in order to stay on the path.
        distance = normalPoint.distance_to(future)
        if distance > path.radius:
            self.seek(target)

        # Draw the debugging stuff
        if self.debug:
            pygame.draw.aaline(self.screen, "black", self.position, future)
            pygame.draw.ellipse(
                self.screen, "gray50", (future.x - 1, future.y - 1, 4, 4)
            )
            pygame.draw.ellipse(
                self.screen, "black", (future.x - 1, future.y - 1, 4, 4), 1
            )

            # Draw normal location
            pygame.draw.aaline(self.screen, "black", future, normalPoint)
            pygame.draw.ellipse(
                self.screen, "gray50", (normalPoint.x - 1, normalPoint.y - 1, 4, 4)
            )
            pygame.draw.ellipse(
                self.screen, "black", (normalPoint.x - 1, normalPoint.y - 1, 4, 4), 1
            )

            if distance > path.radius:
                pygame.draw.ellipse(
                    self.screen, "red", (target.x + b.x - 4, target.y + b.y - 4, 8, 8)
                )
            else:
                pygame.draw.ellipse(
                    self.screen,
                    "gray50",
                    (target.x + b.x - 4, target.y + b.y - 4, 8, 8),
                )

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration += force

    # A method that calculates and applies a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def seek(self, target):
        desired = (
            target - self.position
        )  # A vector pointing from the position to the target

        # If the magnitude of desired equals 0, skip out of here
        # (We could optimize self to check if x and y are 0 to avoid mag() square root
        if desired.magnitude() == 0:
            return

        # Normalize desired and scale to maximum speed
        desired.normalize_ip()
        desired *= self.maxspeed

        # Steering = Desired minus Velocity
        steer = desired - self.velocity
        steer.scale_to_length(self.maxforce)  # Limit to maximum steering force

        self.applyForce(steer)

    # Method to update position
    def update(self):
        if pygame.key.get_just_pressed()[pygame.K_SPACE]:
            self.debug = not self.debug

        # Update velocity
        self.velocity += self.acceleration
        # Limit speed
        self.velocity.scale_to_length(self.maxspeed)
        self.position += self.velocity
        # Reset accelerationelertion to 0 each cycle
        self.acceleration *= 0

    # Wraparound
    def borders(self, p):
        if self.position.x > p.end.x + self.r:
            self.position.x = p.start.x - self.r
            self.position.y = p.start.y + (self.position.y - p.end.y)

    def show(self):
        # Draw a triangle rotated in the direction of velocity
        offset = self.position
        theta = self.velocity.as_polar()[1]

        head = pygame.Vector2(self.r * 2, 0).rotate(theta)
        back_left = pygame.Vector2(-self.r * 2, -self.r).rotate(theta)
        back_right = pygame.Vector2(-self.r * 2, self.r).rotate(theta)

        pygame.draw.polygon(
            self.screen,
            "gray50",
            [head + offset, back_left + offset, back_right + offset],
        )
        pygame.draw.polygon(
            self.screen,
            "black",
            [head + offset, back_left + offset, back_right + offset],
            2,
        )


# A function to get the normal point from position to a line segment (a-b)
# This function could be optimized to make fewer new Vector objects
def getNormalPoint(position, a, b):
    # Vector that points from a to position
    vectorA = position - a

    # Vector that points from a to b
    vectorB = b - a

    # Using the dot product for scalar projection
    vectorB.normalize_ip()
    vectorB *= vectorA.dot(vectorB)

    # Finding the normal point along the line segment
    normalPoint = a + vectorB

    return normalPoint

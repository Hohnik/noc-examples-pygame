# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import pygame

# The "Vehicle" class


class Vehicle:
    def __init__(self, x, y, maxspeed=4, maxforce=0.1):
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
        # Predict location 50 (arbitrary choice) frames ahead
        # This could be based on speed
        future = self.velocity.copy()
        future.scale_to_length(50)
        future += self.position

        # Now we must find the normal to the path from the predicted location
        # We look at the normal for each line segment and pick out the chlosest one
        target = None
        normal = None
        worldRecord = float(
            "inf"
        )  # Start with a very high record distance that can easily be beaten

        # Loop through all points of the path
        for i in range(len(path.points) - 1):
            # Look at a line segment
            a = path.points[i]
            b = path.points[i + 1]

            # Get the normal point to that line
            normalPoint = getNormalPoint(future, a, b)
            # This only works because we know our path goes from left to right
            # We could have a more sophisticated test to tell if the point is in the line segment or not
            if normalPoint.x < a.x or normalPoint.x > b.x:
                # This is something of a hacky solution, but if its not within the line segment
                # Consider the normal to just be the end of the line segment (point b)
                normalPoint = b.copy()

            # How far away are we from the path?
            distance = future.distance_to(normalPoint)
            # Did we beat the record and find the closest line segment?
            if distance < worldRecord:
                worldRecord = distance
                # If so the target we want to steer towards is the normal
                normal = normalPoint
                target = normalPoint.copy()

                # Look at the direction of the line segemnt so we can seek a little bit ahead of the normal
                dir = b - a
                # This is an oversimplification
                # Should be based on distance to path & velocity
                dir.scale_to_length(10)
                target += dir

        # Only if the distance is greater than the path's radius do we bother to steer
        if worldRecord > path.radius and target is not None:
            self.seek(target)

        # Draw the debugging stuff
        if self.debug:
            # Draw predicted future location
            pygame.draw.aaline(self.screen, "black", self.position, future)
            pygame.draw.ellipse(
                self.screen, "gray50", (future.x - 1, future.y - 1, 4, 4)
            )
            pygame.draw.ellipse(
                self.screen, "black", (future.x - 1, future.y - 1, 4, 4), 1
            )

            # Draw normal location
            pygame.draw.aaline(self.screen, "black", future, normal)
            pygame.draw.ellipse(
                self.screen, "gray50", (normal.x - 1, normal.y - 1, 4, 4)
            )
            pygame.draw.ellipse(
                self.screen, "black", (normal.x - 1, normal.y - 1, 4, 4), 1
            )

            if worldRecord > path.radius:
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
        if self.position.x > p.getEnd().x + self.r:
            self.position.x = p.getStart().x - self.r
            self.position.y = p.getStart().y + (self.position.y - p.getEnd().y)

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

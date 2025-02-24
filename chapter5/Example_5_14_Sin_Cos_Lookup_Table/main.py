# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

import math

import pygame

# sincoslookup taken from http://wiki.processing.org/index.php/Sin/Cos_look-up_table
# archived version http://web.archive.org/web/20130510100827/http://wiki.processing.org/w/Sin/Cos_look-up_table
# ported to p5.js by Miká Kruschel
# https://editor.p5js.org/mikakruschel/sketches/Ag6QMqDE

# declare arrays and params for storing sin/cos values
sinLUT = None
cosLUT = None
# set table precision to 0.5 degrees
SC_PRECISION = 0.5
# caculate reciprocal for conversions
SC_INV_PREC = 1 / SC_PRECISION
# compute required table length
SC_PERIOD = math.floor(360 * SC_INV_PREC)
# Conversion factor: degrees to radians
DEG_TO_RAD = math.pi / 180


# init sin/cos tables with values
# should be called from setup()
def initSinCos():
    global sinLUT, cosLUT
    sinLUT = [None for _ in range(SC_PERIOD)]
    cosLUT = [None for _ in range(SC_PERIOD)]
    for i in range(SC_PERIOD):
        sinLUT[i] = math.sin(i * DEG_TO_RAD * SC_PRECISION)
        cosLUT[i] = math.cos(i * DEG_TO_RAD * SC_PRECISION)


# circle radius used for example
radius = None


def setup():
    screen = pygame.display.set_mode((640, 360))
    initSinCos()  # Important call to initialize lookup tables
    return screen


def draw(screen: pygame.Surface, frameCount):
    screen.fill((255, 255, 255))
    mouseX, mouseY = pygame.mouse.get_pos()

    # modulate the current radius
    radius = 50 + 50 * sinLUT[frameCount % SC_PERIOD]

    # draw a circle mad of points (every 5 degrees)
    for i in range(0, 360, 5):
        # convert degrees into array index:
        # the modulo operator (%) ensures periodicity
        theta = int((i * SC_INV_PREC) % SC_PERIOD)

        # draw the circle around mouse pos
        pygame.draw.circle(
            screen,
            "black",
            (mouseX + radius * cosLUT[theta], mouseY + radius * sinLUT[theta]),
            2,
        )


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = setup()
    running = True
    frameCount = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw(screen, frameCount)
        pygame.display.flip()
        clock.tick(60)
        frameCount += 1

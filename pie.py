import math

from numpy.lib.function_base import angle


def checkPoint(percent, x, y):
    # We want to start at the northern side of the circle
    startingAngle = -90
    endingangle = startingAngle + (percent*3.6)

    x = x-50
    y = y-50

    radius = 50

    polarRadius, polarAngle = polarLocation(x, y)

    if(x, y) < (0, 0):
        # print("Left hand sectors")
        # print(endingangle)
        polarAngle = polarAngle + 180
        # print(polarRadius, polarAngle)

    if (polarAngle >= startingAngle and polarAngle <= endingangle and polarRadius <= radius):
        return("black")
    else:
        return("white")


def polarDistance(x, y, radius, angle):
    dx = radius * math.cos(math.radians(angle))
    dy = radius * math.sin(math.radians(angle))
    return (x + dx, y+(-dy))


def polarLocation(x, y):
    if x == 0:
        x = x + 0.0000000000001
    if y == 0:
        y = y + 0.0000000000001

    radius = math.sqrt(x * x + y * y)
    angle = -math.atan(y / x)
    return (radius, math.degrees(angle))


print(checkPoint(50, 25, 25))

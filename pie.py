import math
from re import L

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


def main():
    print("Welcome to the Progress Pie checker!")
    with open('input.txt') as f:
        lines = f.readlines()
        try:
            for line in range(1, int(lines[0])+1):
                values = lines[line].split()
                print(checkPoint(int(values[0]), int(
                    values[1]), int(values[2])))
        except ValueError:
            print("First line was not a number")


if __name__ == '__main__':
    main()

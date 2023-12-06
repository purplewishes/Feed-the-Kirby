import math
EPSILON = 0.000000001


def distance(x0, y0, x1, y1):
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5

def project(vx, vy, tx, ty):
    xProj = (vx * tx + vy * ty) * tx / (tx ** 2 + ty ** 2)
    yProj = (vx * tx + vy * ty) * ty / (tx ** 2 + ty ** 2)

    return xProj, yProj

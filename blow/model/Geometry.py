# -*- coding: utf-8 -*-

import math

def getMoveVectorPoint(x, y):
    if x == 0.0:
        return (0.0, 1.0)
    else:
        alpha = math.atan(y / x)
        if x > 0.0:
            alpha += math.pi
        return (math.cos(alpha), math.sin(alpha))

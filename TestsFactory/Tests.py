__author__ = 'GSUS'
from math import *

def f1(xs):
    sum = 0.0
    for x in xs:
        sum += x**2
    return sum

def f2(xs):
    term1 = xs[0]**2 - xs[1]
    term2 = 1.0 - xs[0]
    return float(100 * term1 * term1 + term2 * term2)

def shekel(xs):
    f5_arr = [[-32.0, -16.0, 0.0, 16.0, 32.0,
              -32.0, -16.0, 0.0, 16.0, 32.0,
              -32.0, -16.0, 0.0, 16.0, 32.0,
              -32.0, -16.0, 0.0, 16.0, 32.0,
              -32.0, -16.0, 0.0, 16.0, 32.0],
             [-32.0, -32.0, -32.0, -32.0, -32.0,
              -16.0, -16.0, -16.0, -16.0, -16.0,
              0.0, 0.0, 0.0, 0.0, 0.0,
              16.0, 16.0, 16.0, 16.0, 16.0,
              32.0, 32.0, 32.0, 32.0, 32.0]]
    x = xs[0]
    y = xs[1]
    s = 0.0


    for i in range(0,25):
        diff1 = x - f5_arr[0][i]
        diff2 = y - f5_arr[1][i]
        subsum = diff1**6 + diff2**6
        subsum += i+1.0
        subsum = 1.0/subsum
        s += subsum

    return 500.0 - (1.0 / (0.002 + s))

def rana(xs):
    RANA_WEIGHTS = [0.3489, 0.1848, 0.3790, 0.4386, 0.9542, 0.1430, 0.7849, 0.3689, 0.9767, 0.8163]
    RANA_SUM_WEIGHTS = 5.3953
    sum = 0.0
    for i in range(len(xs)):
        x1 = xs[i]
        x2 = xs[(i+1) % len(xs)]
        sum += RANA_WEIGHTS[i] * (x1 * sin(sqrt(fabs(x2 + 1.0 - x1))) *\
                                   cos(sqrt(fabs(x1 + x2 + 1.0))) + (x2 + 1.0) *\
                                   cos(sqrt(fabs(x2 + 1.0 - x1))) *\
                                   sin(sqrt(fabs(x1 + x2 + 1.0))))
    return sum / RANA_SUM_WEIGHTS

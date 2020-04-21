#!/usr/bin/env python3
import sys
import math
import os


def usage(exit_code=0):
    progname = os.path.basename(sys.argv[0])
    print(
        f'usage: {progname} sumX sumY sum(xSquare) sum(ySquare) sumXY, yHat, xStar, n, tStat')
    sys.exit(exit_code)


def findSXX(xi, x2, n):
    return (x2 - (pow(xi, 2) / n))


def findSYY(yi, y2, n):
    return (y2 - (pow(yi, 2) / n))


def findSXY(xy, xi, yi, n):
    return (xy - ((xi*yi) / n))


def findB1(sxy, sxx):
    return sxy/sxx


def findSSE(syy, b1, sxy):
    return syy-(b1*sxy)


def findSE(sse, n):
    return math.sqrt(abs(sse/(n-2)))


def findCI(y, tStat, sy):
    lower = y - tStat*sy
    upper = y + tStat*sy
    print(f'({lower:.4f},{upper:.4f})')


def findSy(x, xBar, sxx, n, se):
    return se * math.sqrt(1 + (1/n) + (pow(x-xBar, 2)/sxx))


def main():

    if (sys.argv[1] == "-h"):
        usage(0)

    xi = float(sys.argv[1])
    yi = float(sys.argv[2])
    x2 = float(sys.argv[3])
    y2 = float(sys.argv[4])
    xy = float(sys.argv[5])
    yHat = float(sys.argv[6])
    xStar = float(sys.argv[7])
    n = float(sys.argv[8])
    t = float(sys.argv[9])

    sxx = findSXX(xi, x2, n)
    syy = findSYY(yi, y2, n)
    sxy = findSXY(xy, xi, yi, n)

    b1 = findB1(sxy, sxx)

    sse = findSSE(syy, b1, sxy)

    se = findSE(sse, n)

    sy = findSy(xStar, xi/n, sxx, n, se)

    findCI(yHat, t, sy)


# Main Execution
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys
import math
import os


def usage(exit_code=0):
    progname = os.path.basename(sys.argv[0])
    print(
        f'usage: {progname} successX successY totalX totalY ...')
    sys.exit(exit_code)


def twoPopPropTest(x, y, m, n):
    p1 = x/m
    p2 = y/n
    p = (x+y)/(m+n)
    num = p1 - p2
    denom = math.sqrt(p*(1-p)*(1/m + 1/n))

    print(f'numer: {num:.4f}')
    print(f'demom: {denom:.4f}')

    return(num/denom)


def main():

    if (sys.argv[1] == "-h"):
        usage(0)

    x = int(sys.argv[1])
    y = int(sys.argv[2])
    m = int(sys.argv[3])
    n = int(sys.argv[4])

    print(f' Test Statistic: {twoPopPropTest(x, y, m, n):.4f}')

# Main Execution


if __name__ == '__main__':
    main()

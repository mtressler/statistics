#!/usr/bin/env python3
import sys
import math


def twoPopPropTest(x, y, m, n):
    p1 = x/m
    p2 = y/n
    p = (x+y)/(m+n)
    num = p1 - p2
    denom = math.sqrt(p*(1-p)*(1/m + 1/n))

    return(num/denom)


def main():

    x = float(sys.argv[1])
    y = float(sys.argv[2])
    m = float(sys.argv[3])
    n = float(sys.argv[4])

    print(f' Test Statistic: {twoPopPropTest(x, y, m, n):.4f}')

# Main Execution


if __name__ == '__main__':
    main()

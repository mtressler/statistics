#!/usr/bin/env python3
import sys
import math


def findTestStat(d, s, n, mu):
    num = (d - mu)
    denom = s/math.sqrt(n)

    return(num/denom)


def main():

    d = float(sys.argv[1])
    s = float(sys.argv[2])
    n = float(sys.argv[3])
    mu = float(sys.argv[4])

    print(f'Test Statistic: , {findTestStat(d, s, n, mu):.4f}')
    print(f'Degrees of Freedom: {n-1}')

# Main Execution


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys
import math
import os


def usage(exit_code=0):
    progname = os.path.basename(sys.argv[0])
    print(
        f'usage: {progname} meanOfDifferences hNullValue(subtracted from meanOfDifferences) stdOfDifferences numPairs ...')
    sys.exit(exit_code)


def findTestStat(d, s, n, mu):
    num = (d - mu)
    denom = s/math.sqrt(n)

    return(num/denom)


def main():

    if (sys.argv[1] == "-h"):
        usage(0)

    d = float(sys.argv[1])
    s = float(sys.argv[2])
    n = float(sys.argv[3])
    mu = float(sys.argv[4])

    print(f'Test Statistic: , {findTestStat(d, s, n, mu):.4f}')
    print(f'Degrees of Freedom: {n-1}')

# Main Execution


if __name__ == '__main__':
    main()

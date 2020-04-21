#!/usr/bin/env python3
import sys
import math
import os


def usage(exit_code=0):
    progname = os.path.basename(sys.argv[0])
    print(
        f'usage: {progname} r n')
    sys.exit(exit_code)


def findTestStat(r, n):
    return (r*math.sqrt(n-2)) / (math.sqrt(1-pow(r, 2)))


def main():

    if (sys.argv[1] == "-h"):
        usage(0)

    r = float(sys.argv[1])
    n = float(sys.argv[2])

    tStat = findTestStat(r, n)

    print(f'Test Statistic: {tStat:.4f}')
    print(f'Degrees of Freedom: {n-2}')


# Main Execution
if __name__ == '__main__':
    main()

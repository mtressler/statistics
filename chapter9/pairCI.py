#!/usr/bin/env python3
import sys
import math
import os


def usage(exit_code=0):
    progname = os.path.basename(sys.argv[0])
    print(
        f'usage: {progname} meanOfDifferences stdOfDifferences numPairs ...')
    sys.exit(exit_code)


def findCI(d, s, n, crit):
    left = d
    right = crit*(s/(math.sqrt(n)))

    val1 = left + right
    val2 = left - right

    if (val1 > val2):
        print(f'({val2:.4f} , {val1:.4f})')
    else:
        print(f'({val1:.4f} , {val2:.4f})')


def main():

    if (sys.argv[1] == "-h"):
        usage(0)

    d = float(sys.argv[1])
    s = float(sys.argv[2])
    n = float(sys.argv[3])
    crit = float(sys.argv[4])

    findCI(d, s, n, crit)

# Main Execution


if __name__ == '__main__':
    main()

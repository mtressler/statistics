#!/usr/bin/env python3
import sys
import math
import os


def usage(exit_code=0):
    progname = os.path.basename(sys.argv[0])
    print(
        f'usage: {progname} meanX1 meanX2 (stdDev/stdErr)X1 (stdDev/stdErr)X2 sizeX1 sizeX2 ...')
    sys.exit(exit_code)


def findCISD(x1, x2, s1, s2, m, n, critVal):
    left = x1 - x2
    a = pow(s1, 2)/m
    b = pow(s2, 2)/n
    right = critVal*math.sqrt(a+b)

    val1 = left + right
    val2 = left - right

    if (val1 > val2):
        print(f'({val2:.4f} , {val1:.4f})')
    else:
        print(f'({val1:.4f} , {val2:.4f})')


def findCISE(x1, x2, s1, s2, critVal):
    left = x1 - x2
    right = critVal*math.sqrt(pow(s2, 2)+pow(s1, 2))

    val1 = left + right
    val2 = left - right

    if (val1 > val2):
        print(f'({val2:.4f} , {val1:.4f})')
    else:
        print(f'({val1:.4f} , {val2:.4f})')


def findDF(s1, s2, m, n):
    a = (s1*s1)/m
    b = (s2*s2)/n
    num = (a+b)*(a+b)
    c = (a*a)/(m-1)
    d = (b*b)/(n-1)
    denom = c+d
    return num/denom


def main():

    if (sys.argv[1] == "-h"):
        usage(0)

    x1 = float(sys.argv[1])
    x2 = float(sys.argv[2])
    s1 = float(sys.argv[3])
    s2 = float(sys.argv[4])
    m = float(sys.argv[5])
    n = float(sys.argv[6])

    print("Degrees of Freedom: ", int(findDF(s1, s2, m, n)))

    critVal = input("Enter Critical Value: ")

    method = input("std dev or std err (d/e): ")

    if method == "d":
        findCISD(x1, x2, s1, s2, m, n, float(critVal))
    elif method == "e":
        findCISE(x1, x2, s1, s2, float(critVal))

# Main Execution


if __name__ == '__main__':
    main()

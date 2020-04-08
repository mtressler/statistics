#!/usr/bin/env python3
import sys
import math


def findCI(x, y, m, n, critVal):
    p1 = x/m
    p2 = y/n
    left = p1 - p2
    right = critVal*math.sqrt(((p1*(1-p1))/m) + ((p2*(1-p2))/n))

    val1 = left + right
    val2 = left - right

    if (val1 > val2):
        print(f'({val2:.4f} , {val1:.4f})')
    else:
        print(f'({val1:.4f} , {val2:.4f})')


def main():

    x = float(sys.argv[1])
    y = float(sys.argv[2])
    m = float(sys.argv[3])
    n = float(sys.argv[4])

    critVal = input("Enter Critical Value: ")

    findCI(x, y, m, n, float(critVal))

# Main Execution


if __name__ == '__main__':
    main()

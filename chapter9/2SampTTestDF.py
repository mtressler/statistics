#!/usr/bin/env python3
import sys
import math


def twoSampTTestSD(x1, x2, mu, s1, s2, m, n):
    num = (x1 - x2 - mu)
    a = pow(s1, 2)/m
    b = pow(s2, 2)/n
    denom = math.sqrt(a+b)

    return(num/denom)


def twoSampTTestSE(x1, x2, mu, s1, s2):
    num = (x1 - x2 - mu)
    denom = math.sqrt(pow(s2, 2)+pow(s1, 2))

    return(num/denom)


def findDF(s1, s2, m, n):
    a = (pow(s1, 2))/m
    b = (pow(s2, 2))/n
    num = pow(a+b, 2)
    denom = pow(b, 2)/(n-1) + pow(a, 2)/(m-1)
    return num/denom


def main():

    x1 = float(sys.argv[1])
    x2 = float(sys.argv[2])
    mu = float(sys.argv[3])
    s1 = float(sys.argv[4])
    s2 = float(sys.argv[5])
    m = float(sys.argv[6])
    n = float(sys.argv[7])

    method = input("std dev or std err (d/e): ")

    if method == "d":
        print("Test Statistic: ", round(
            twoSampTTestSD(x1, x2, mu, s1, s2, m, n), 4))
    elif method == "e":
        print("Test Statistic: ", round(
            twoSampTTestSE(x1, x2, mu, s1, s2), 4))

    print("Degrees of Freedom: ", findDF(s1, s2, m, n))

# Main Execution


if __name__ == '__main__':
    main()

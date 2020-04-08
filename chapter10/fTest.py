#!/usr/bin/env python3
import sys
import math


def xBar(size, mean, totalSize):

    sampMean = 0

    for n, x in zip(size, mean):
        sampMean += (n*x)

    return sampMean/totalSize


def sstr(size, mean, sampMean):

    total = 0

    for n, x in zip(size, mean):
        total += n*pow(x-sampMean, 2)

    return total


def sse(size, SD):

    total = 0

    for n, s in zip(size, SD):
        total += (n-1)*pow(s, 2)

    return total


def sst(sstr, sse):
    return sstr + sse


def mstr(sstr, numTreat):

    return sstr/(numTreat - 1)


def mse(sse, numTotal, numTreat):

    return sse/(numTotal - numTreat)


def fStat(mstr, mse):

    return mstr/mse


def main():

    numTreat = int(sys.argv[1])
    arguments = sys.argv[2:]
    size = []
    mean = []
    SD = []
    n = 0

    i = 2

    for treat in range(1, numTreat+1):
        size.append(int(sys.argv[i]))
        n += int(sys.argv[i])
        i += 1
        mean.append(float(sys.argv[i]))
        i += 1
        SD.append(float(sys.argv[i]))
        i += 1

    sampMean = xBar(size, mean, n)

    treatSS = sstr(size, mean, sampMean)

    errorSS = sse(size, SD)

    totalSS = sst(treatSS, errorSS)

    msTreat = mstr(treatSS, numTreat)

    msError = mse(errorSS, n, numTreat)

    testStat = fStat(msTreat, msError)

    print(f'Fcdf({testStat:.4f},E99,{numTreat-1},{n-numTreat})')

# Main Execution


if __name__ == '__main__':
    main()

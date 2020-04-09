#!/usr/bin/env python3
import sys
import math
import os


def usage(exit_code=0):
    progname = os.path.basename(sys.argv[0])
    print(
        f'usage: {progname} numValues sizeLowestMean lowestMean sizeNextLowestMean nextLowestMean sizeNextLowestMean nextLowestMean ... sizeHighestMean highestMean MSE Q')
    sys.exit(exit_code)


def sigDif(size, mean, mse, q):
    copySize = size
    copyMean = mean
    testNum = 1

    copySize.pop(0)
    copyMean.pop(0)

    for x, n in list(zip(mean, size)):
        findW(x, n, copyMean, copySize, mse, q, testNum)

        testNum += 1
        copySize.pop(0)
        copyMean.pop(0)


def findW(meanVal, sizeVal, meanList, sizeList, mse, q, testNum):

    w = 0
    meandif = 0
    sig = 0

    for x, n in zip(meanList, sizeList):
        print(f'Test Number {testNum}')
        w = q*math.sqrt((mse/2)*((1/n) + (1/sizeVal)))
        meanDif = x - meanVal
        sig = w - meanDif
        print(f'{meanVal} , {x}')

        if (sig > 0):
            print(f'{w:.4f} - {meanDif:.4f} = {sig:.4f}')
            print(f'No significant difference')
        else:
            print(f'{w:.4f} - {meanDif:.4f} = {sig:.4f}')
            print(f'There is a significant difference')


def main():

    if (sys.argv[1] == "-h"):
        usage(0)

    numMeans = int(sys.argv[1])
    size = ['0']
    mean = ['0']
    mse = 0
    q = 0

    i = 2

    for num in range(1, numMeans+1):
        size.append(int(sys.argv[i]))
        i += 1
        mean.append(float(sys.argv[i]))
        i += 1

    mse = float(sys.argv[i])
    i += 1
    q = float(sys.argv[i])

    sigDif(size, mean, mse, q)

# Main Execution


if __name__ == '__main__':
    main()

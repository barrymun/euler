from __future__ import division


def isPrime(n):
    """
    concise method: https://stackoverflow.com/a/4117879
    """
    if n < 2:
        return False

    if n == 2:
        return True

    if n & 1 == 0:
        return False

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True


def generateSpiral():
    """
    """
    start = 1

    primeCount = 0
    totalCount = 1
    ratio = 1.0
    spiralLength = 1

    right = start
    top = start
    left = start
    bottom = start

    rightOffset = 2
    topOffset = 4
    leftOffset = 6
    bottomOffset = 8

    offset = 8

    while ratio >= 0.1:
        right += rightOffset
        top += topOffset
        left += leftOffset
        bottom += bottomOffset

        # print right, top, left, bottom

        if isPrime(n=right):
            primeCount += 1
        if isPrime(n=top):
            primeCount += 1
        if isPrime(n=left):
            primeCount += 1
        if isPrime(n=bottom):
            primeCount += 1

        rightOffset += offset
        topOffset += offset
        leftOffset += offset
        bottomOffset += offset

        totalCount += 4

        ratio = primeCount / totalCount

        spiralLength += 2

    return spiralLength


if __name__ == "__main__":
    print generateSpiral()

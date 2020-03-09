import math


def f(n):
    """
    """
    return math.factorial(n)


def combinatoricSelection(n, r):
    """
    n! / r!(n - r)!, where r <= n and 0! = 1
    """
    if r > n:
        return 0
    return f(n=n) / (f(n=r) * f(n=(n - r)))


if __name__ == "__main__":
    print combinatoricSelection(n=5, r=3)
    print combinatoricSelection(n=23, r=10)

    limit = 100
    count = 0

    for i in xrange(0, limit + 1):
        for j in xrange(i, limit + 1):
            # print j,i
            if combinatoricSelection(n=j, r=i) > 1000000:
                count += 1
    print count

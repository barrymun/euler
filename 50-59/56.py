def powerOf(n, p):
    """
    """
    r = 1
    while p > 0:
        r *= n
        p -= 1
    return r


def getDigitalSum(n):
    """
    """
    l = ''.join(str(n))
    l = [int(x) for x in l]
    return sum(l) if len(l) > 0 else 0


if __name__ == "__main__":
    print powerOf(3, 2)
    print powerOf(3, 3)

    lower = 1
    upper = 99
    ans = 0
    for i in xrange(lower, upper + 1):
        for j in xrange(lower, upper + 1):
            p = powerOf(n=i, p=j)
            ds = getDigitalSum(n=p)
            if ds > ans:
                ans = ds
    print ans

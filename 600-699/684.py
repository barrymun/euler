from __future__ import division

LIMIT = 90


def s(n):
    """
    """
    if n == 0:
        return 0
    i = 1
    while True:
        if sum([int(x) for x in str(i)]) == n:
            break
        # if len(n)
        i += 1
    return i


def s2(n):
    """
    *** much faster
    """
    if n < 10:
        # covering 1 -> 9 inclusive
        return n
    r = ""
    while n > 9:
        r += "9"
        n -= 9
    if n > 0:
        r = str(n) + r
    return r


def s3(n):
    """
    """

    lenN = len(str(n))
    mul = ""
    while len(mul) < (lenN - 1):
        mul += "9"

    if lenN < 2:
        # covering 1 -> 9 inclusive
        return n

    r = ""
    while n > 9:
        r += mul
        n -= int(mul)
        if (len(mul) >= len(str(n))) and (len(mul) > 1):
            mul = mul[:-1]
    if n > 0:
        r = str(n) + r
    return r


def S(n):
    """
    """
    r = 0
    while n > 0:
        # r += int(s2(n=n))
        r += int(s3(n=n))
        n -= 1
    return r


def constructMap():
    """
    """
    i = 2
    m = {
        0: 0,
        1: 1,
    }
    while i <= LIMIT:
        m[i] = m[i - 2] + m[i - 1]
        i += 1
    return m


if __name__ == "__main__":
    pass
    # print s(10)
    # print s(20)
    # print s(30)
    # print s(40)
    # print s(50)
    # print ""
    # print s2(10)
    # print s2(20)
    # print s2(30)
    # print s2(40)
    # print s2(50)
    # print ""

    print ""
    print s2(10)
    print s3(10)
    print S(20)
    print ""

    m = constructMap()
    mod = 1000000007
    i = 2
    r = 0
    while i <= LIMIT:
        print i, r
        r += S(n=m[i])
        i += 1
    print "---"
    print r
    print "---"
    print r / mod
    print "---"

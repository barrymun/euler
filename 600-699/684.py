from __future__ import division

LIMIT = 90


# def s(n):
#     """
#     """
#     if n == 0:
#         return 0
#     i = 1
#     while True:
#         if sum([int(x) for x in str(i)]) == n:
#             break
#         i += 1
#     return i


# def s2(n):
#     """
#     *** much faster
#     """
#     if n < 10:
#         # covering 1 -> 9 inclusive
#         return str(n)
#     r = ""
#     while n > 9:
#         r += "9"
#         n -= 9
#     if n > 0:
#         r = str(n) + r
#     return r


def s3(n):
    """
    *** much faster v3
    """

    lenN = len(str(n))
    mul = ""
    while len(mul) < (lenN - 1):
        mul += "9"

    if lenN < 2:
        # covering 1 -> 9 inclusive
        return str(n)

    r = ""
    while n > 9:
        r += mul
        n -= int(mul)
        if (len(mul) >= len(str(n))) and (len(mul) > 1):
            mul = mul[:-1]
    if n > 0:
        r = str(n) + r
    return r


# def S(n):
#     """
#     """
#     r = 0
#     while n > 0:
#         # r += int(s2(n=n))
#         r += int(s3(n=n))
#         n -= 1
#     return r


def S2(n, cursor=0, prev=0):
    """
    """
    r = 0
    while n > cursor:
        r += int(s3(n=n))
        n -= 1
    return r + prev


def constructMap():
    """
    creates the fibonacci sequence of numbers
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

    print ""
    # print s2(10)
    print s3(10)
    print s3(11)
    print s3(20)
    print S2(n=20)
    print ""
    # raise Exception

    m = constructMap()
    print m
    # raise Exception

    mod = 1000000007
    i = 2
    r = 0
    prev = 0
    cursor = 0
    while i <= LIMIT:
        # print i, r, prev, cursor
        print i, r
        prev = S2(n=m[i], cursor=cursor, prev=prev)
        cursor = m[i]
        r += prev
        i += 1
    print "---r---"
    print r
    print "---r%mod---"
    print r % mod
    # print "---r/mod---"
    # print r / mod
    # print "---"

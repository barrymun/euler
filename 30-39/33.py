from __future__ import division

MIN = 10
MAX = 99

def is_curious_fraction(numerator, denominator):
    """
    """
    if numerator >= denominator:
        return False

    n_list = [int(i) for i in str(numerator)]
    d_list = [int(i) for i in str(denominator)]

    if 0 in n_list or 0 in d_list:
        return False

    match = None
    for i in n_list:
        if i in d_list:
            match = i

    if match is None:
        return False

    n_list.remove(match)
    d_list.remove(match)

    if (n_list[0] >  d_list[0]):
        return False

    if ((numerator / denominator) != (n_list[0] / d_list[0])):
        return False

    return True

if __name__ == "__main__":
    r = []
    for i in xrange(MIN, MAX + 1):
        for j in xrange(MIN, MAX + 1):
            if is_curious_fraction(numerator=j, denominator=i):
                r.append((j, i))
    print r

    numerator = 1
    denominator = 1

    for t in r:
        n, d = t
        numerator *= n
        denominator *= d

    print numerator / denominator
    print "{} / {}".format(numerator, denominator)

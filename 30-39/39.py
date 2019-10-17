import math

def is_rat(a, b, c):
    """
    is right angled triangle
    c = sqrt(a^2 + b^2)
    """
    return float(c) == float(math.sqrt(((a * a) + (b * b))))

if __name__ == "__main__":
    p = 120
    r = {}
    # TODO: slow
    while p <= 1000:
        r[p] = []
        exit = False
        for a in xrange(1, 999):  # > 1, < 998 (min len == 1 for other sides)
            for b in xrange(1, 999):
                c = p - (a + b)

                if (b, a, c) in r[p]:
                    # we can exit both for loops at this point,
                    # as the inverses have already been accounted for
                    exit = True
                    break

                if not is_rat(a, b, c):
                    continue

                if ((a, b, c) not in r[p] and (b, a, c) not in r[p]):
                    r[p].append((a, b, c))

            if exit:
                break

        p += 1
        print p

    max = 0
    val = 0
    for k, v in r.items():
        if len(v) > max:
            max = len(v)
            val = k

    print max
    print val

MAX_LEN = 9
DIGIT_CHECK = [str(i) for i in xrange(1, 10)]

def is_pandigital(n):
    """
    """
    if len(n) > MAX_LEN or len(n) < MAX_LEN:
        return False

    check = True
    for digit in DIGIT_CHECK:
        if digit not in n:
            check = False
            break
    # if check:
    #     print n
    return check

if __name__ == "__main__":
    r = []
    for i in xrange(11, 100):
        for j in xrange(111, 1000):
            p = i * j

            # if (len("{}{}{}".format(i, j, p)) > MAX_LEN or len("{}{}{}".format(i, j, p)) < MAX_LEN):
            #     # all numbers beyond this point will be greater, so better to exit the loop
            #     break

            if not is_pandigital(n="{}{}{}".format(i, j, p)):
                continue

            r.append(p)

    print ""
    print len(r)
    r = list(set(r))
    print len(r)

    print ""
    print r
    print sum(int(n) for n in r)

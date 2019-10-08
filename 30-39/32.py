import time

MAX_LEN = 9
DIGIT_CHECK = [str(i) for i in xrange(1, 10)]

def is_pandigital(n):
    """
    """
    if len(n) > MAX_LEN or len(n) < MAX_LEN:
        # sanity check
        return False

    # can do this but seems to be slower
    # return set(DIGIT_CHECK) == set(n)

    check = True
    for digit in DIGIT_CHECK:
        if digit not in n:
            check = False
            break
    # if check:
    #     print n
    return check

if __name__ == "__main__":
    start = time.time()
    r = []

    # single digit
    for i in xrange(1, 10):
        for j in xrange(111, 10000):
            p = i * j
            n = "{}{}{}".format(i, j, p)
            if (len(n) > MAX_LEN):
                # all numbers beyond this point will be greater, so better to exit the loop to improve efficiency
                break
            if not is_pandigital(n=n):
                continue
            r.append(p)

    for i in xrange(11, 100):
        for j in xrange(111, 1000):
            p = i * j
            n = "{}{}{}".format(i, j, p)
            if (len(n) > MAX_LEN or len(n) < MAX_LEN):
                # all numbers beyond this point will be greater, so better to exit the loop to improve efficiency
                break
            if not is_pandigital(n=n):
                continue
            r.append(p)

    r = list(set(r))  # removing duplicates
    print sum(int(n) for n in r)  # answer

    end = time.time()
    print end - start

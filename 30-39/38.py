MAX_LEN = 9
DIGIT_CHECK = [str(i) for i in xrange(1, 10)]

def derive_pandigital(n):
    """
    """
    r = ""
    x = 1
    while len(r) < 9:
        r += str(n * x)
        x += 1
    return r

def has_pandigital_multiples(n):
    """
    """
    r = ""
    x = 1
    while len(r) < 9:
        r += str(n * x)
        x += 1

    if is_pandigital(n=r):
        return True

    return False

def is_pandigital(n):
    """
    """
    n = str(n)

    if len(n) > MAX_LEN or len(n) < MAX_LEN:
        # sanity check
        return False

    # can do this but seems to be slower
    return set(DIGIT_CHECK) == set(n)
    # ...

    check = True
    for digit in DIGIT_CHECK:
        if digit not in n:
            check = False
            break
    return check

if __name__ == "__main__":
    i = None
    for i in xrange(9, 98766):
        if has_pandigital_multiples(n=i):
            r = i

    print r
    print derive_pandigital(n=r)

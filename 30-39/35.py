UPPER_LIMIT = 1000000

def is_prime(n):
    """
    concise method: https://stackoverflow.com/a/4117879
    TODO: look into pollard rho brent integer factorisation algorithm
    """
    if n == 1:
        return False

    if n & 1 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True


def get_multiple(n):
    """
    """
    r = 10
    for i in xrange(1, n):
        r *= 10
    return r

def is_circular_prime(n):
    """
    """
    if not is_prime(n=n):
        return False

    valid = True
    l = len(str(n))
    for i in xrange(1, l):
        remainder = n % 10
        temp = int(n / 10)
        n = (remainder * get_multiple(n=l-1)) + temp
        if not is_prime(n=n):
            valid = False
            break

    return valid

if __name__ == "__main__":
    # accounting for 2
    r = [2]
    for i in xrange(1, 1000000):
        if is_circular_prime(n=i):
            r.append(i)

    print len(r)

from math import sqrt
from itertools import count, islice

def is_prime(n):
    """
    """
    if n < 2:
        return False

    if n == 2:
        return True

    if n & 1 == 0:
        return False

    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True

def cut_prime(n):
    """
    """
    valid = True

    temp = n
    temp /= 10
    while temp > 0:
        if not is_prime(n=temp):
            valid = False
            break
        temp /= 10

    if not valid:
        return False

    # get reverse, convert back to integer
    rev = int(str(n)[::-1])
    rev /= 10
    while rev > 0:
        un_rev = int(str(rev)[::-1])
        if not is_prime(n=un_rev):
            valid = False
            break
        rev /= 10

    return valid

def gen_primes():
    """
    Sieve of Eratosthenes
    Code by David Eppstein, UC Irvine, 28 Feb 2002
    http://code.activestate.com/recipes/117119/
    https://stackoverflow.com/a/568618
    """

    D = {}
    q = 2
    while True:
        if q not in D:
            if q > 7:
                # for this problem:
                # 2, 3, 5, and 7 are not considered to be truncatable primes
                yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

if __name__ == "__main__":
    # [_ for _ in gen_primes()]

    s = 0
    count = 0
    for r in gen_primes():
        valid = cut_prime(n=r)
        if not valid:
            continue

        print r
        s += r
        count += 1
        if count >= 11:
            break

    print s

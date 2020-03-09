def isPrime(n):
    """
    concise method: https://stackoverflow.com/a/4117879
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


def genPrimes():
    """
    https://stackoverflow.com/a/568618
    """
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def hasConsecutiveDistinctPrimeFactors2(n, primes):
    for f1 in primes:
        for f2 in primes:
            if f1 == f2:
                continue
            if f1 * f2 > n:
                break
            if f1 * f2 == n:
                return True
    return False


def hasConsecutiveDistinctPrimeFactors3(n, primes):
    for f1 in primes:
        for f2 in primes:
            if f1 * f2 > n:
                break
            for f3 in primes:
                if f1 == f2 or f2 == f3 or f1 == f3:
                    continue
                if f1 * f2 * f3 > n:
                    break
                if f1 * f2 * f3 == n:
                    return True
    return False


def hasConsecutiveDistinctPrimeFactors4(n, primes):
    for f1 in primes:
        for f2 in primes:
            if f1 * f2 > n:
                break
            for f3 in primes:
                if f1 * f2 * f3 > n:
                    break
                for f4 in primes:
                    if f1 * f2 * f3 * f4 > n:
                        break
                    if f1 == f2 or f2 == f3 or f3 == f4 or f1 == f4 or f1 == f3 or f2 == f4:
                        continue
                    if f1 * f2 * f3 * f4 == n:
                        return True
    return False


if __name__ == "__main__":
    # lower = 10
    # upper = 100
    # requiredCount = 2

    # lower = 100
    # upper = 1000
    # requiredCount = 3

    lower = 1000
    upper = 10000
    requiredCount = 4

    primes = []
    for p in genPrimes():
        if p > upper:
            break
        primes.append(p)

    print(len(primes))
    primes = primes[:int(lower / requiredCount)]
    print(len(primes))

    # print primes

    acc = []
    for n in xrange(lower, upper):
        if len(acc) == requiredCount:
            break
        r = hasConsecutiveDistinctPrimeFactors4(n=n, primes=primes)
        if not r:
            acc = []
            continue
        acc.append(n)

    print acc

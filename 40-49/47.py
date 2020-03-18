def primeFactors(n):
    """
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def distinctPrimeFactors(n):
    """
    """
    return list(set(primeFactors(n=n)))


def distinctTotalPrimeFactors(n):
    """
    """
    return len(distinctPrimeFactors(n=n))


if __name__ == "__main__":
    count = 0
    match = 4
    start = 1000

    i = start
    while count < match:
        if distinctTotalPrimeFactors(n=i) == match:
            count += 1
        else:
            count = 0
        i += 1
    print i - match

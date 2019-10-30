import operator

def gen_primes():
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

if __name__ == "__main__":
    """
    NOTE: consecutive primes don't have to start at 2
    """
    limit = 1000000

    primes = []
    total = 0
    for p in gen_primes():
        total += p
        if total >= limit:
            break
        primes.append(p)

    print primes
    print len(primes)
    print ''

    sequences = []
    index = 1
    while index <= len(primes):
        for i in xrange(0, len(primes[:index])):
            total = 0
            seq = []
            for j in xrange(i, len(primes[:index])):
                seq.append(primes[:index][j])
            sequences.append(seq)
        index += 1

    r = {
        "value": 0,
        "count": 0,
    }
    for sequence in sequences:
        temp = 0
        for s in sequence:
            temp += s

        if (temp > r.get("value")) \
            and (is_prime(n=temp)) \
            and (len(sequence) >= r.get("count")):
            r["value"] = temp
            r["count"] = len(sequence)

    print r

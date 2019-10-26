from itertools import permutations

BASE = '9876543210'
PRIMES = [2, 3, 5, 7, 11, 13, 17]

def generate_pandigitals():
    """
    """
    # just chose 7654321 as 9 and 8 digits had no relevant primes
    return [''.join(list(t)) for t in list(permutations(BASE))]

def has_pattern(s = ''):
    """
    """
    assert len(s) == len(BASE)
    d1 = 1
    d2 = 2
    d3 = 3

    r = True
    index = 0
    while d3 < 10:
        n = int('{}{}{}'.format(s[d1], s[d2], s[d3]))
        if n % PRIMES[index] != 0:
            r = False
            break

        d1 += 1
        d2 += 1
        d3 += 1
        index += 1
    return r

if __name__ == "__main__":
    pn = generate_pandigitals()
    print len(pn)

    print has_pattern(s='1406357289')

    r = 0
    for s in pn:
        if has_pattern(s=s):
            r += int(s)
    print r

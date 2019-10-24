from itertools import permutations

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

def generate_pandigitals():
    """
    """
    # just chose 7654321 as 9 and 8 digits had no relevant primes
    return [''.join(list(t)) for t in list(permutations("7654321"))]

if __name__ == "__main__":
    r = 0
    for n in generate_pandigitals():
        n = int(n)
        if not is_prime(n=n):
            continue
        if n > r:
            r = n
    print r

from math import sqrt

def get_pentagonal_number(n):
    """
    """
    return (n * ((3 * n) - 1)) / 2

def is_pentagonal(n):
    """
    https://en.wikipedia.org/wiki/Pentagonal_number#Tests_for_pentagonal_numbers
    """
    k = (sqrt(24 * n + 1) + 1) / 6
    return k.is_integer()

if __name__ == "__main__":
    r = 0
    j = 1

    while r == 0:
        pj = get_pentagonal_number(n=j)
        j += 1

        for k in xrange(j, 0, -1):
            pk = get_pentagonal_number(n=k)
            s = pj + pk
            d = abs(pj - pk)

            if is_pentagonal(n=s) and is_pentagonal(n=d):
                r = d
                break

    print r

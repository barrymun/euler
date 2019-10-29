import sys

def get_pentagonal_number(n):
    """
    """
    return (n * ((3 * n) - 1)) / 2

def generate_pentagonal_numbers(upper_limit):
    """
    """
    p_numbers = []
    for i in xrange(1, upper_limit):
        pn = get_pentagonal_number(n=i)
        p_numbers.append(pn)
    return p_numbers

if __name__ == "__main__":
    l = 3000

    r = 0
    pn = generate_pentagonal_numbers(upper_limit=l)

    for j in xrange(1, l):
        if r != 0:
            break

        for k in xrange(j, l):
            pj = get_pentagonal_number(n=j)
            pk = get_pentagonal_number(n=k)
            s = pj + pk
            d = abs(pj - pk)

            if s in pn and d in pn:
                r = d
                break

    print r

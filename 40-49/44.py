import sys

tracker = {}

def get_pentagonal_number(n):
    """
    """
    return (n * ((3 * n) - 1)) / 2

def generate_pentagonal_numbers(upper_limit):
    """
    """
    i = 1  # index
    pn = 0  # pentagonal number
    while pn < upper_limit:
        pn = get_pentagonal_number(n=i)
        if pn not in tracker:
            tracker[pn] = True
        i += 1

if __name__ == "__main__":
    r = 0

    for k in xrange(1, 500):
        if r != 0:
            break

        for j in xrange(1, 500):

            pk = get_pentagonal_number(n=k)
            pj = get_pentagonal_number(n=j)

            s = pk + pj
            d = pk - pj
            d = abs(d)
            # print pk, pj, s, d


            gen_pn = generate_pentagonal_numbers(upper_limit=s)
            # print tracker
            # sys.exit()
            if s in tracker and d in tracker:
                print pk, pj, s, d
                print tracker[s], tracker[d]
                r = d
                break

    print r

from itertools import permutations

def is_prime(n):
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

def get_permutations(n):
    """
    """
    s = str(n)
    p_tuples = list(permutations(s))
    p_lists = [list(i) for i in p_tuples]
    p_strings = [''.join(i) for i in p_lists]

    # remove any number less than 1000
    new_p_strings = []
    for i in p_strings:
        if int(i) >= 1000:
            new_p_strings.append(i)

    p_strings = new_p_strings

    tracker = {}
    for i in xrange(0, len(p_strings)):
        for j in xrange(i, len(p_strings)):
            key = str(abs(int(p_strings[i]) - int(p_strings[j])))
            val = (p_strings[i], p_strings[j])
            if key not in tracker:
                tracker[key] = [val]
            else:
                tracker[key].append(val)
    # print tracker

    for k, v in tracker.items():
        if len(v) < 2:
            continue
        val_tuples_as_lists = [list(i) for i in v]
        flat_vals = [i for sublist in val_tuples_as_lists for i in sublist]
        unique_vals = list(set(flat_vals))
        if len(unique_vals) == 3:
            check = True
            for i in unique_vals:
                if not is_prime(n=int(i)):
                    check = False
                    break
            if check:
                return unique_vals

    return None

if __name__ == "__main__":
    x = get_permutations(n=1487)
    print x

    r = None
    for i in xrange(1000, 10000):
        x = get_permutations(n=i)
        if x is not None:
            print x
            # break
    print r

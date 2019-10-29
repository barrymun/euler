def get_power_of(n):
    """
    """
    r = 1
    i = 1
    while i <= n:
        r *= n
        i += 1
    return r

if __name__ == "__main__":
    r = 0
    for i in xrange(1, 1001):
        r += get_power_of(n=i)
    print r

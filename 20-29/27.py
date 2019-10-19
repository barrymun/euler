A_MAX = 1000
B_MAX = 1001
N_MAX = 100

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

def calc(a, b):
    """
    formula: n^2 + an + b where abs(a) < 1000 and abs(b) <= 1000
    """
    count = 0
    for n in xrange(0, N_MAX):
        x = (n * n) + (a * n) + b
        if x < 0:
            x *= -1
        if not is_prime(n=x):
            break
        count += 1
    return count

if __name__ == "__main__":
    r = {
        "count": 0,
        "a": 0,
        "b": 0,
    }

    for a in xrange(1, A_MAX):
        for b in xrange(1, B_MAX):
            count = calc(a=a, b=b)
            if count > r.get("count"):
                r["count"] = count
                r["a"] = a
                r["b"] = b

    for a in xrange(1, A_MAX):
        for b in xrange(1, B_MAX):
            count = calc(a=a*-1, b=b)
            if count > r.get("count"):
                r["count"] = count
                r["a"] = a*-1
                r["b"] = b

    for a in xrange(1, A_MAX):
        for b in xrange(1, B_MAX):
            count = calc(a=a, b=b*-1)
            if count > r.get("count"):
                r["count"] = count
                r["a"] = a
                r["b"] = b*-1

    for a in xrange(1, A_MAX):
        for b in xrange(1, B_MAX):
            count = calc(a=a*-1, b=b*-1)
            if count > r.get("count"):
                r["count"] = count
                r["a"] = a*-1
                r["b"] = b*-1

    print r
    x = r.get("a") * r.get("b")
    print x

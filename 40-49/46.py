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

def twice_square_leaves_prime(n):
    """
    """
    base = 2
    square = 1

    check = False
    while True:
        squared = square * square
        square += 1
        c = 2 * squared

        if c >= n:
            break

        if is_prime(n=(n - c)):
            check = True
            break

    return check

if __name__ == "__main__":
    r = 0
    i = 9
    while True:
        if (i % 2 != 0) and (not is_prime(n=i)):
            if not twice_square_leaves_prime(n=i):
                r = i
                break
        i += 1

    print r

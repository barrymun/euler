def isPrime(n):
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


if __name__ == "__main__":
    pass

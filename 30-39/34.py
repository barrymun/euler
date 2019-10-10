import math


def is_sum_of_factorial_of_digits(n):
    """
    """
    if n == 1 or n == 2:
        return False

    n_as_list = [int(i) for i in str(n)]

    factorial_sum = 0
    for i in n_as_list:
        f = math.factorial(i)
        factorial_sum += f

    if factorial_sum != n:
        return False

    return True


if __name__ == "__main__":
    r = 0
    for i in xrange(1, 1000000):
        if is_sum_of_factorial_of_digits(n=i):
            r += i

    print r

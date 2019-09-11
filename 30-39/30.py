POWER = 5
MIN = 0
MAX = 999999

def power_of(n, exp=POWER):
    r = 1
    i = 0
    while i < exp:
        r *= n
        i += 1
    return r

def get_sum_of_powers(n):
    digits = []
    while (n > 0):
        digits.append(n % 10)
        n /= 10
    digits = [power_of(i) for i in digits]
    r = 0
    for i in digits:
        r += i
    return r

def is_sum_of_powers(n):
    return get_sum_of_powers(n) == n

if __name__ == "__main__":
    sums = []
    for i in range(MIN, MAX + 1):
        if is_sum_of_powers(i):
            sums.append(get_sum_of_powers(i))
    print sums
    r = 0
    for i in sums:
        r += i
    r -= 1  # subtract the 1 as this is not permitted
    print r

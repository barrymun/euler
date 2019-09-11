MIN = 2
MAX = 100

def power_of(n, exp):
    r = 1
    i = 0
    while i < exp:
        r *= n
        i += 1
    return r

def get_combinations(n):
    r = []
    for i in range(MIN, MAX + 1):
        x = power_of(n, i)
        r.append(x)
    return r

if __name__ == "__main__":
    r = []
    for i in range(MIN, MAX + 1):
        x = get_combinations(i)
        r = r + x
    r = list(set(r))
    print len(r)

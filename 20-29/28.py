N = 1001

def c():
    r = 0
    counter = 0
    multiple = 2
    offset = 2

    while True:
        if r == 0:
            r += 1
            counter += 1
            continue

        if counter > 3:
            counter = 0
            offset += 2

        x = (multiple + 1)
        if x > (N * N):
            break
        r += x
        multiple += offset
        counter += 1
    return r


if __name__ == "__main__":
    r = c()
    print r

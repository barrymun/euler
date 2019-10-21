def generate_fraction():
    """
    """
    i = 1
    s = "0"
    while i < 1000000:
        s += str(i)
        i += 1
    return s

if __name__ == "__main__":
    r = generate_fraction()
    print int(r[1])
    print int(r[10])
    print int(r[100])
    print int(r[1000])
    print int(r[10000])
    print int(r[100000])
    print int(r[1000000])
    print int(r[1]) * \
        int(r[10]) * \
        int(r[100]) * \
        int(r[1000]) * \
        int(r[10000]) * \
        int(r[100000]) * \
        int(r[1000000])

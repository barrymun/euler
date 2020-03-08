def containsSameDigits(x, y):
    """
    """
    return ''.join(sorted(str(x))) == ''.join(sorted(str(y)))


def findSmallestMultiple():
    """
    """
    n = 1
    multiplier = 2
    while True:
        if multiplier > 6:
            break
        if not containsSameDigits(x=n, y=(n * multiplier)):
            n += 1
            continue
        else:
            multiplier += 1
    return n


if __name__ == "__main__":
    r = findSmallestMultiple()
    print r

def isNumeratorLonger(num, den):
    """
    """
    return len(str(num)) > len(str(den))


def calc():
    """
    """
    num = 3
    den = 2

    count = 0
    i = 1
    while i <= 1000:
        if isNumeratorLonger(num=num, den=den):
            count += 1
        nextNum = num + (den * 2)
        nextDen = num + den
        num = nextNum
        den = nextDen
        i += 1
    return count


if __name__ == "__main__":
    print calc()

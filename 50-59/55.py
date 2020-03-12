def isPalindrome(n):
    """
    """
    return str(n) == str(n)[::-1]


def isLychrel(n):
    """
    """
    count = 0
    p = n
    while count < 50:
        if isPalindrome(n=p) and count != 0:
            break
        count += 1
        p += int(str(p)[::-1])

    if count == 50:
        return True
    return False


if __name__ == "__main__":
    print('---')
    # print isPalindrome(n=4774)
    # print isPalindrome(n=4773)
    print isLychrel(n=196)
    print isLychrel(n=4994)

    lychrelCount = 0
    n = 1
    while n <= 10000:
        if isLychrel(n=n):
            lychrelCount += 1
        n += 1
    print lychrelCount

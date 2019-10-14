def is_palindrome(n):
    """
    """
    return str(n) == str(n)[::-1]

def convert_integer_to_binary(n):
    """
    stripping the '0b' from the begininning of the string
    """
    return bin(n)[2:]

if __name__ == "__main__":
    r = 0
    for i in xrange(0, 1000000):
        if not is_palindrome(n=str(i)):
            continue
        if not is_palindrome(n=convert_integer_to_binary(n=i)):
            continue
        r += i
    print r

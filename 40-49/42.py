import os
import sys

N_CHARS = 26  # the number of letters in the alphabet
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_triangle_numbers(n):
    """
    get the first "n" triangle numbers
    """
    r = []
    for i in xrange(1, n + 1):
        t = ((i * (i + 1)) / 2)
        r.append(t)
    return r

def is_triangle_number(word = '', t_numbers = []):
    """
    """
    x = 0
    for char in word:
        index = ALPHABET.index(char.lower())
        value = index + 1
        x += value

    if x in t_numbers:
        return True
    return False

def read_words():
    """
    """
    with open(os.path.join(sys.path[0], 'words.txt'), 'r') as f:
        line = f.readline()
        return line.split(',')

if __name__ == "__main__":
    words = read_words()
    print len(words)

    # replace quotes
    words = [w.replace('"', '') for w in words]

    max_len = 0
    for w in words:
        if len(w) > max_len:
            max_len = len(w)
    print max_len

    t_numbers = get_triangle_numbers(n=max_len * N_CHARS)
    print len(t_numbers)

    print is_triangle_number(word='SKY', t_numbers=t_numbers)

    count = 0
    for w in words:
        if is_triangle_number(word=w, t_numbers=t_numbers):
            count += 1
    print count

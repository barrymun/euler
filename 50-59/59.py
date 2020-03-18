import os
import sys


asciiMap = {
    65: "A",
    66: "B",
    67: "C",
    68: "D",
    69: "E",
    70: "F",
    71: "G",
    72: "H",
    73: "I",
    74: "J",
    75: "K",
    76: "L",
    77: "M",
    78: "N",
    79: "O",
    80: "P",
    81: "Q",
    82: "R",
    83: "S",
    84: "T",
    85: "U",
    86: "V",
    87: "W",
    88: "X",
    89: "Y",
    90: "Z",
}

def read():
    """
    """
    l = []
    with open(os.path.join(sys.path[0], 'p059_cipher.txt'), 'r') as f:
        for line in f:
            l = line.split(',')
    return l


if __name__ == "__main__":
    l = read()
    print len(l)
    s= ""
    for i in l:
        if int(i) >= 65 and int(i) <= 90:
            s += asciiMap.get(int(i))
    print s

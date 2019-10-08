import itertools

COINS = [
    1,
    2,
    5,
    10,
    20,
    50,
    100,
    200,
]

if __name__ == "__main__":
    print list(itertools.permutations(COINS))

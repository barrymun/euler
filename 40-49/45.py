def get_triangular_number(n):
    """
    """
    return (n * (n + 1)) / 2

def get_pentagonal_number(n):
    """
    """
    return (n * ((3 * n) - 1)) / 2

def get_hexagonal_number(n):
    """
    """
    return n * ((2 * n) - 1)

def generate_triangular_numbers(upper_limit):
    """
    """
    t_numbers = []
    for i in xrange(1, upper_limit):
        tn = get_triangular_number(n=i)
        t_numbers.append(tn)
    return t_numbers

def generate_pentagonal_numbers(upper_limit):
    """
    """
    p_numbers = []
    for i in xrange(1, upper_limit):
        pn = get_pentagonal_number(n=i)
        p_numbers.append(pn)
    return p_numbers

def generate_hexagonal_numbers(upper_limit):
    """
    """
    h_numbers = []
    for i in xrange(1, upper_limit):
        hn = get_hexagonal_number(n=i)
        h_numbers.append(hn)
    return h_numbers

if __name__ == "__main__":
    tn = generate_triangular_numbers(upper_limit=100000)
    pn = generate_pentagonal_numbers(upper_limit=100000)
    hn = generate_hexagonal_numbers(upper_limit=100000)

    tp = list(set(tn).intersection(pn))
    ph = list(set(pn).intersection(hn))
    shared = list(set(tp).intersection(ph))
    print shared

from itertools import permutations

INDEX = 1000000

def convert_permutation_tuple_to_int(t):
	tuple_as_list = list(t)
	l = [str(i) for i in tuple_as_list]
	return int(''.join(l))

if __name__ == "__main__":
	r = []
	n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	perm = permutations(n)
	for i in list(perm):
		r.append(convert_permutation_tuple_to_int(i))
	print(len(r))
	print(r[INDEX - 1])

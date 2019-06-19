MAX_ABUNDANT_SUM = 28123

def is_abundant(n):
	max_divisor = int(n / 2) + 1
	sum = 0
	for i in range(1, max_divisor):
		if (n % i != 0):
			continue
		sum += i
	return sum > n

def get_abundants():
	return [i for i in range(1, MAX_ABUNDANT_SUM) if is_abundant(i)]

def sum_pos_integers_not_sum_of_two_abundants():
	r = {i: 0 for i in range(1, MAX_ABUNDANT_SUM)}
	abundants = get_abundants()
	for i in range(0, len(abundants)):
		for j in range(i, len(abundants)):
			abundant_sum = abundants[i] + abundants[j]
			if abundant_sum > MAX_ABUNDANT_SUM:
				continue
			r[abundant_sum] = abundant_sum
	return r

if __name__ == "__main__":
	s = sum_pos_integers_not_sum_of_two_abundants()
	count = 0
	for k, v in s.items():
		if v != 0:
			continue
		count += k
	print(count)

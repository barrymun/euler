def fact(n):
	r = 1
	while n > 0:
		r *= n
		n -= 1
	return r

def sum(n):
	r = 0
	while n > 0:
		r += n % 10
		n /= 10
	return r


if __name__ == "__main__":
	f = fact(100)
	s = sum(f)
	print(s)


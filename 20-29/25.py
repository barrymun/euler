TERMS = {}

def get_fibonacci_term(n):
	if n < 1:
		return 0
	if n == 1 or n == 2:
		return 1
	
	if (n - 1) in TERMS:
		f1 = TERMS[n - 1]
	else:
		f1 = get_fibonacci_term(n - 1)
		TERMS[n - 1] = f1
	
	if (n - 2) in TERMS:
		f2 = TERMS[n - 2]
	else:
		f2 = get_fibonacci_term(n - 2)
		TERMS[n - 2] = f2
	
	return f1 + f2

if __name__ == "__main__":
	n = 3
	while True:
		# print(n)
		r = get_fibonacci_term(n)
		if len(str(r)) >= 1000:
			print(n)
			break
		n += 1

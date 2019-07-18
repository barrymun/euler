START = 123456789
END = 9876543210

def contains_all_digits(n):
	n = str(n)
	if ('1' in n) and \
		('2' in n) and \
		('3' in n) and \
		('4' in n) and \
		('5' in n) and \
		('6' in n) and \
		('7' in n) and \
		('8' in n) and \
		('9' in n):
		if ('0' in n) or (len(n) < 10):
			return True
		else:
			return False
	else:
		return False

def get_millionth_lex_perm():
	r = 0
	count = 0
	i = START
	while i <= END:
		i += 1
		if not contains_all_digits(i):
			continue
		count += 1
		print(i)
		if count == 1000000:
			r = i
			break
		if count == 10:
			break
	return r

if __name__ == "__main__":
	# print(contains_all_digits(123456789))
	# print(contains_all_digits(876543219))
	a = get_millionth_lex_perm()
	print(a)

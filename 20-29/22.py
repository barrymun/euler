SCORE = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
	'e': 5,
	'f': 6,
	'g': 7,
	'h': 8,
	'i': 9,
	'j': 10,
	'k': 11,
	'l': 12,
	'm': 13,
	'n': 14,
	'o': 15,
	'p': 16,
	'q': 17,
	'r': 18,
	's': 19,
	't': 20,
	'u': 21,
	'v': 22,
	'w': 23,
	'x': 24,
	'y': 25,
	'z': 26,
}

def read():
	f = open("names.txt", "r")
	l = []
	for line in f:
		l = line.split(',')
	return l

def format(l):
	for index, i in enumerate(l):
		i = i.replace('"', '').lower()
		l[index] = i
	return l

def alphabetical_sort(l):
	l.sort(key=str.lower)
	return l

def get_value(s, index):
	r = 0
	for i in s:
		r += SCORE.get(i)
	return r * (index + 1)

if __name__ == "__main__":
	r = read()
	f = format(r)
	l = alphabetical_sort(f)

	sum = 0
	for index, i in enumerate(l):
		sum += get_value(i, index)

	print(sum)

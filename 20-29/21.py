def d(n):
	r = 0;
	for i in range(1, n):
		if n % i != 0:
			continue
		r += i
	return r

def divisor_sum(n):
	r = {}
	for i in range(1, n):
		r[i] = d(i)
	return r

def amicable_pairs(d):
	r = []
	for k, v in d.items():
		if k == v:
			continue
		compare = d.get(v, None)
		if compare is None:
			continue
		if k != compare:
			continue
		r.append(k)
		r.append(v)
	return list(set(r))

def sum(l):
	count = 0
	for i in l:
		count += i
	return count

if __name__ == "__main__":
	# t1 = d(284)
	# t2 = d(220)
	# print(t1)
	# print(t2)
	r1 = divisor_sum(9999)
	r2 = amicable_pairs(r1)
	r3 = sum(r2)
	print(r3)
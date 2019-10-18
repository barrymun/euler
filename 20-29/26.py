from __future__ import division

from decimal import *

getcontext().prec = 10000  # set the percision of the decimal calculations


# def repeats(s):
# 	"""
# 	https://stackoverflow.com/a/29489919
# 	"""
# 	i = (s+s).find(s, 1, -1)
# 	return None if i == -1 else s[:i]

def repeats(s):
	"""
	"""
	for x in range(1, len(s)):
		ss = s[:x]
		if ss * (len(s)//len(ss))+(ss[:len(s)%len(ss)]) == s:
			if (len(ss) > int(len(s) / 2)):
				return ''
			return ss
	return ''

def get_recurring_cycle_string(n):
	"""
	"""
	x = str(Decimal(1) / Decimal(n))
	x = x[2:]  # remove the 0.
	x = x[:-1]  # remove the last character which will affect the recurring sequence
	return x

if __name__ == "__main__":
	# print get_recurring_cycle_string(n=6)
	# print get_recurring_cycle_string(n=7)
	# print repeats(s='0045662100456621004566210045662100456621')
	# print repeats(s='14285714285714285714285714285714285714285')

	max_len = 0
	r = None
	for i in xrange(1, 1001):
		s = get_recurring_cycle_string(n=i)
		rs = repeats(s=s)
		if len(rs) > max_len:
			max_len = len(rs)
			r = i

	print max_len
	print r

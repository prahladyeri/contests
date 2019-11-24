import sys
for line in sys.stdin:
	itr = int(line)
	res = (2**itr + 1) ** 2
	print(res)

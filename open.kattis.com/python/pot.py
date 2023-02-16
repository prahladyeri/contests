import sys, math
nc = 0
total = 0
line,expected = 0,0
for input in sys.stdin:
	if expected == 0:
		ar = input.split()
		nc = int(ar[0])
		expected = nc
		total = 0
	else:
		ar = input.split()
		base = int(ar[0][:-1])
		exp = int(ar[0][-1:])
		total += math.pow(base,exp)
		line += 1
		if line >= expected:
			line = 0
			expected = 0
			print(round(total))

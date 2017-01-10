import sys, datetime
nc, problems = 0,0
line = 0
expected = 0
for input in sys.stdin:
	if expected == 0:
		ar = input.split()
		nc, problems = int(ar[0]), int(ar[1])
		expected = nc
	else:
		line += 1
		if line >= expected:
			line = 0
			expected = 0
			print(problems)

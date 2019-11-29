import sys
import math

i = 0
tot, n, at_bats = 0, 0, []
for line in sys.stdin:
	if i == 0:
		n = int(line.strip())
	else:
		line = line.split(" ")
		at_bats = [int(i) for i in line]
		for j in at_bats:
			if j == -1:
				n -= 1
			else:
				tot += j
		print(tot/n)
	i += 1

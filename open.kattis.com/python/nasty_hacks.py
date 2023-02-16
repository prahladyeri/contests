import sys

i = 0
for line in sys.stdin:
	if i == 0:
		n = int(line)
	else:
		vals = [int(s) for s in line.split()]
		rwa, ra, c = vals
		if (ra - c ) > rwa:
			print("advertise")
		elif (ra - c) < rwa:
			print("do not advertise")
		else:
			print("does not matter")
			
	i += 1

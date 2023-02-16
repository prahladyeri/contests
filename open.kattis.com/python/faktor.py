import sys, math

for line in sys.stdin:
	line = line.split()
	n, c = int(line[0]), int(line[1])
	c = (c - 1) + 0.01
	res = c * n
	print( math.ceil(res) )

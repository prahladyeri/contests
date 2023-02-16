import sys

for line in sys.stdin:
	line = line.split()
	a, b = line[0], line[1]
	ar = "".join( [a[i] for i in range(len(a)-1, -1, -1)] )
	br = "".join( [b[i] for i in range(len(b)-1, -1, -1)] )
	ar, br = int(ar), int(br)
	if ar > br:
		print(ar)
	else:
		print(br)

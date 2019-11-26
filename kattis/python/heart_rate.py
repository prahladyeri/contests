import sys

i = 0
for line in sys.stdin:
	if i > 0:
		line = line.split()
		b, p = int(line[0]), float(line[1])
		x = 60 / p
		print("%.4f %.4f %.4f" % (x*b-x, x*b, x*b+x))
	i += 1

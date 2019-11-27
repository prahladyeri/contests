import sys
for line in sys.stdin:
	line = line.split()
	x, y = int(line[0]), int(line[1])
	if y%2 != 0: #y is odd
		print("impossible")
	else:
		print("possible")
	#print(x, y)

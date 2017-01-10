import sys

for index,line in enumerate(sys.stdin):
	if index == 0: continue
	n = int(line)
	print("%d is %s" % (n, "even" if n%2==0 else "odd"))
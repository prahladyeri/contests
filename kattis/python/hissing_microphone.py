import sys

for line in sys.stdin:
	line, hiss = line.strip(), False
	for i in range(len(line)):
		if i > 0 and line[i] == 's' and line[i-1] == 's':
			hiss = True
			print("hiss")
			break
	if not hiss: print("no hiss")

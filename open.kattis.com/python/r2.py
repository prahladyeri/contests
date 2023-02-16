import sys

for input in sys.stdin:
	inp = input.split()
	R1 = int(inp[0])
	S = int(inp[1])
	R2 = S*2 - R1
	print(R2)

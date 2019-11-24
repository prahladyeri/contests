import sys

for input in sys.stdin:
	#print("".join([name[0] for name in input.split('-')]))
	inp = input.split()
	R1 = int(inp[0])
	S = int(inp[1])
	#S = (R1+R2)/2
	#S*2 = (R1+R2)
	#S*2 - R = R2
	R2 = S*2 - R1
	print(R2)

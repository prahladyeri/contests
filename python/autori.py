import sys

for input in sys.stdin:
	print("".join([name[0] for name in input.split('-')]))
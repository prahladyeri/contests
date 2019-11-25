import sys

i = 0
for line in sys.stdin:
	if i == 0:
		n = int(line)
	else:
		num = int(line)
		for i in range(num-1, 1, -1):
			num *= i
		print(str(num)[-1])
			
	i += 1

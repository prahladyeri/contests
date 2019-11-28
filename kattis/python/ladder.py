import sys
import math

for line in sys.stdin:
	line = line.split()
	h, v = int(line[0]), int(line[1])
	# sine(v) = opp/hypotenuse
	sine_val = math.sin(math.radians(v))
	hypotenuse = math.ceil(h/sine_val)
	print(hypotenuse)

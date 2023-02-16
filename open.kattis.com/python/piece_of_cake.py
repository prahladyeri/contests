import sys

def mul(lst):
	val = 1
	for num in lst:
		val *= num
	return val

for line in sys.stdin:
	lines = line.split(" ")
	n, h, v = int(lines[0]), int(lines[1]), int(lines[2])
	height = 4 #constant
	
	#let's define all pieces from clock-wise in terms of (l,b,h)
	#horizontal=length, vertical=breadth
	c1 = (h, v, height)
	c2 = (h, n-v, height)
	c3 = (n-h, n-v, height)
	c4 = (n-h, v, height)
	
	#let's calculate their values
	ll = [mul(c1), mul(c2), mul(c3), mul(c4)]
	ll.sort()
	print(ll[-1])

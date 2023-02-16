l,r = input().split()
l,r = int(l), int(r)

if l == 0 and r == 0:
	print("Not a moose")
elif l == r:
	print("Even", l+r)
elif l != r:
	mx = max(l,r)
	print("Odd", mx*2)

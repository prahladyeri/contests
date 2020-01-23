l, h = input().split()
l, h = int(l), int(h)
n = 0
for i in range(l, h+1):
	divisible = True
	for c in str(i):
		if str(i).count(c) > 1: #1st condition
			divisible = False
			break
		elif int(c) == 0: 
			divisible = False
			break
		elif  (i % int(c)) != 0: #3nd condition
			divisible = False # not perfectly divisible
			break
	if divisible: 
		n+= 1

print(n)

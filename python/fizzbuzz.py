import sys

for line in sys.stdin:
	ar = line.split()
	x,y,n = int(ar[0]),int(ar[1]),int(ar[2])
	for i in range(1,n+1):
		str1 = ""
		str1 = "Fizz" if i%x == 0 else ""
		str1 += "Buzz" if i%y == 0 else ""
		print(i if len(str1) == 0 else str1)
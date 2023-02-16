def main():
	n = int(input())
	sum = n #234
	#for i in range(n, 0, -1):
	digits = 0
	while(sum>=1):
		sum /= 10
		#print(sum)
		digits += 1
	print(digits)
	
main()

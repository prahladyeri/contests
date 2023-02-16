#!/usr/bin/env python3
l = []

def fibonacci(n, k):
	if n <= k:
		l.append(1)
		return 1
	else:
		sm = sum(l[n-k-1:])
		l.append(sm)
		return sm
		
	
if __name__ == "__main__":
	#n = int(input())
	#k = int(input())
	n,k = [int(x) for x in input().split()]
	for i in range(1, n+1):
		res = fibonacci(i, k)
		#print(i,res)
	res = (res % 1000000007)
	print(res)
		

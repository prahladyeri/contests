#work in progress
cnt = 1
cases = int(input())
for i in range(cases):
	k, b, n =input().split()
	b,n = int(b), int(n)
	#print('b:', b)
	a_series, tot = [], 0
	j = 0
	for c in str(n):
		a_series.append(int(c)/b**j)
		j += 1
	print(a_series)
	for j in range(len(a_series)):
		tot += (a_series[j] ** 2)
	print(tot)

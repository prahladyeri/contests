#work in progress
cnt = 1
cases = int(input())
for i in range(cases):
	k, b, n =input().split()
	tot = 0
	for c in str(n):
		tot += int(c)**2
	print(tot)

	
	b,n = int(b), int(n)
	a_series, tot, pw = [], 0, 0
	while(tot<=n):
		a = (b**pw)
		pw += 1


n = int(input())
for i in range(0, n):
	a, b = input(), input()
	ss = ""
	for j in range(len(a)):
		ss += '.' if a[j] == b[j] else '*'
	print(a)
	print(b)
	print(ss, "\n")

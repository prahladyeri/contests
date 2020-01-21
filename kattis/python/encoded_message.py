import textwrap, math

cnt = int(input())

for case in range(cnt):
	ss = input()
	n = int(math.sqrt(len(ss)))
	parts = textwrap.wrap(ss, n)
	nss = ""
	for i in range(n-1, -1, -1):
		for j in range(n):
			nss += parts[j][i]
	print(nss)

l, x = input().split()
l, x = int(l), int(x)
cnt, deny_cnt = 0, 0
for i in range(x):
	verb, n = input().split()
	n = int(n)
	if verb == "enter":
		if (n + cnt) > l: #exceeds limit, deny entry
			deny_cnt += 1
		else:
			cnt += n
	elif verb == "leave":
		cnt -= n

print(deny_cnt)

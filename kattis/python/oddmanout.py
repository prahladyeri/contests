cases = int(input())
for case in range(1, cases+1):
	ll = []
	n, ppl = int(input()), input().split()
	for c in ppl:
		if not c in ll:
			ll.append(c)
		else:
			ll.remove(c)
	print("Case #%d: %s" % (case, ll[0]))

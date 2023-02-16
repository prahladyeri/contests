cases = int(input())
for case in range(cases):
	extra = 0
	seq = input().split()
	seq = [int(c) for c in seq]
	for i in range(len(seq)):
		if i == 0: continue
		if seq[i] == 0: break
		mx = seq[i-1] * 2
		if seq[i] > mx: extra += (seq[i]-mx)
	print(extra)

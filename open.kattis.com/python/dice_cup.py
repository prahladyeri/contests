import sys, math


for line in sys.stdin:
	line = line.split()
	n, m = int(line[0]), int(line[1])
	outcomes = []
	poss = {}
	for i in range(1, n+1):
		for j in range(1, m+1):
			outcomes.append((i+j))
	for o in outcomes:
		if o not in poss.keys(): poss[o] = 0
		poss[o] += 1
	poss = sorted(poss.items(), key=lambda x: x[1])
	mx_prob = poss[-1][1]
	poss = [item for item in poss if item[1] == mx_prob]
	for i in range(len(poss)):
		print(poss[i][0])

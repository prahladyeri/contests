n = int(input())
univs = []
acnt = 0

for i in range(n):
	ss = input()
	univ,team = ss.split()
	if univ in univs: continue
	univs.append(univ)
	print(univ, team)
	acnt += 1
	if acnt == 12: break

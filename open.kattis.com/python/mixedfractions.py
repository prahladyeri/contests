while(True):
	ss = input()
	if ss == "0 0": break
	a,b = ss.split()
	a,b = int(a), int(b)
	whole = int(a/b)
	numer = a%b
	print(whole, numer, "/", b)

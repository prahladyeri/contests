ss = input()
tcnt, ccnt, gcnt = ss.count("T"), ss.count("C"), ss.count("G")
out = tcnt**2 + ccnt**2 + gcnt**2
if tcnt != 0 and ccnt != 0 and gcnt != 0:
	mm = min([tcnt,ccnt,gcnt])
	out += 7 * mm
print(out)

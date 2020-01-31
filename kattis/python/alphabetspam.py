import math

ss = input()
cats = [0,0,0,0]
cnt = len(ss)

for i in range(cnt):
	o = ord(ss[i])
	if o == 95: # _
		cats[0] += 1
	elif o >= 97 and o <= 122: #lowercase
		cats[1] += 1
	elif o >= 65 and o<= 90:
		cats[2] += 1
	else:
		cats[3] += 1

print(round(cats[0]/cnt, 15))
print(round(cats[1]/cnt, 15))
print(round(cats[2]/cnt, 15))
print(round(cats[3]/cnt, 15))

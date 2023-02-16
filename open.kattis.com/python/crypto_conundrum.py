cipher = input()
ss = int(len(cipher)/3) * "PER"
n = 0
for i in range(len(cipher)):
	if cipher[i] == ss[i]:
		pass # no need to change
	else:
		n += 1
print(n)

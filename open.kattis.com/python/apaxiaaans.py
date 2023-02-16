ss = input()
out = ss[0]
for i in range(1, len(ss)):
	if ss[i] != ss[i-1]: out += ss[i]
print(out)

#work in progress

ss, key = input(), input()

#key = key + ss
#key = key[0:len(ss)]

# SGZVQBUQAFRWSLC

out = ""
print('key:',key)
for i in range(len(ss)):
	o = ord(ss[i])
	#shift = ord(key[i]) - 65
	shift = ord(ss[i]) #- 65
	val = o - shift # o + shift
	#if val < 65: val += 67
	#if val > 90: val-= 26
	n = chr(val)
	out += n
	print('ss[i], o, shift, val, n:', ss[i], o, shift, val, n)

print(out)

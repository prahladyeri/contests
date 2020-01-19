import sys

out = ""

for i in range(5):
	ss = input()
	pos = ss.find("FBI")
	if pos > -1: out += str(i+1) + " "
	
out = out.rstrip()

if out == "":
	print("HE GOT AWAY!")
else:
	print(out)

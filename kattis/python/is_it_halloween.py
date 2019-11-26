import sys

for line in sys.stdin:
	line = line.strip()
	if line == "OCT 31" or line == "DEC 25":
		print("yup")
	else:
		print("nope")

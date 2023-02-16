n, a, b = int(input()), input(), input()

if n % 2 == 0: # even, a and b should be equal
	if a == b:
		print("Deletion succeeded")
	else:
		print("Deletion failed")
else:
	fail = False
	for i in range(len(a)):
		c = a[i]
		e = '0' if c == '1' else '1' #expected
		if b[i] != e:
			fail = True
			break
	if fail:
		print("Deletion failed")
	else:
		print("Deletion succeeded")

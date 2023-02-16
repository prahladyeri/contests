cnt = 1
while True:
	n = int(input())
	if n == 0: break
	head, tail = [], []
	for i in range(n):
		word = input()
		if i%2 == 0: #even
			head.append(word)
		else:
			tail.append(word)
	# ~ print(head)
	# ~ print(tail)
	print("SET %d" % cnt)
	for i in range(len(head)):
		print(head[i])
	for i in range(len(tail)-1, -1, -1):
		print(tail[i])
	cnt += 1

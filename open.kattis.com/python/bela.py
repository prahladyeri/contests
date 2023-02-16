vals = {
	'A': [11, 11],
	'K': [4, 4],
	'Q': [3, 3],
	'J': [20, 2],
	'T': [10, 10],
	'9': [14, 0],
	'8': [0, 0],
	'7': [0, 0],
}
line = input().split()
n, s = int(line[0]), line[1]
pts = 0
for i in range(4*n):
	ln = input()
	des, suit = ln[0], ln[1]
	if suit == s: #dominant
		pts += vals[des][0]
	else:
		pts += vals[des][1]
print(pts)

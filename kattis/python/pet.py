import sys

out = ""
mpos, mpts = 0,0
for i in range(5):
	ss = input().split()
	pts = [int(j) for j in ss]
	pts = sum(pts)
	if pts > mpts:
		mpts = pts
		mpos = i+1

print(mpos, mpts)

#!/usr/bin/env python3

if __name__ == "__main__":
	lines = [input() for i in range(int(input()))]
	for line in lines:
		ca,cb = 0,0
		lastpos,neut,vills = '',0,list(line)
		for i in range(len(vills)):
			vill = vills[i]
			if vill == 'A':
				ca += 1
				if neut != 0 and lastpos == 'A': ca += neut
				lastpos,neut ='A',0
			elif vill == 'B':
				cb += 1
				if neut != 0 and lastpos == 'B': cb += neut
				lastpos,neut ='B',0
			else:
				neut += 1
		print("%d %d" % (ca, cb))

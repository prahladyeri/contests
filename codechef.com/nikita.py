#!/usr/bin/env python3

if __name__ == "__main__":
	lines = [input() for i in range(int(input()))]
	for line in lines:
		r, words = "", line.split()
		for i in range(len(words)):
			if i == len(words)-1:
				r += words[i].capitalize()
			else:
				r += words[i][0].upper() + ". "
		print(r)

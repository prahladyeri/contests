#!/usr/bin/env python3

if __name__ == "__main__":
	lines = [input() for i in range(int(input()) *2)]
	for i in range(0, len(lines),2):
		n = int(lines[i])
		strips = lines[i+1]
		strips = strips.split()
		#print('processing:',n,"::",strips)
		result = ''
		if n % 2 ==0 or int(strips[0]) != 1:
			result = "no"
		else:
			start, expected, result = int(strips[0]), 0, 'yes'
			#print("start is %d" % start)
			for i in range(int(n/2)+1):
				expected = start + i
				if int(strips[i]) != expected:
					#print(i, "*expected: %d, but actual: %d" % (expected, int(strips[i])))
					result = 'no'
					break
			#print("Expected is %d in the middle." % expected)
			if result != 'no':
				for i in range(int(n/2)+1,n):
					expected -= 1
					if int(strips[i]) != expected:
						#print(i, "#expected: %d, but actual: %d" % (expected, int(strips[i])))
						result = 'no'
						break
		print(result)
				

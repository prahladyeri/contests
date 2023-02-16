def main():
	tot, ss = 0, input()
	power = len(ss)
	for i in map(int, ss): tot += (i**power)
	print(tot==int(ss))
	
main()

def main():
	tot, ss = 0, input()
	for i in map(int, ss): tot += (i**3)
	print(tot==int(ss))
	
main()

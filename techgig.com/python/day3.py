def main():
	b = float(input()) #initial balance
	r = int(input()) #rate of interest
	n = int(input()) #no. of years
	i = b * (r/100) * n
	print(int(i))

main()

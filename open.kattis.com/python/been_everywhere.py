import sys, datetime

n_cases = int(input())

for i in range(n_cases):
	n, cities = int(input()), []
	for j in range(n):
		city = input()
		if not city in cities: cities.append(city)
	print(len(cities))

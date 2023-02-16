def main():
	n = input()
	arr = input().split(" ")
	arr = [int(i) for i in arr]
	arr.remove(max(arr))
	print(max(arr))
	
main()

n = int(input())
ls = input().split()
ls = [int(item) for item in ls]

mn = min(ls)
print(ls.index(mn))

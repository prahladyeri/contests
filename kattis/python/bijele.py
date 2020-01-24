coll = input().split() #collection
icoll = [1,1,2,2,2,8] #ideal collection
out = ""

for i in range(len(coll)):
	coll[i] = int(coll[i])

for i in range(len(coll)):
	diff = icoll[i] - coll[i]
	out += str(diff) + " "
	
print(out.rstrip())

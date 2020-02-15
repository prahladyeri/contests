bp = [3,2,1] #buying power
g,s,c = input().split()
g,s,c = int(g), int(s), int(c)
tbp = g*bp[0] + s*bp[1] + c*bp[2]
ss = ""
#victory cards
if tbp >= 8:
	ss += "Province"
elif tbp >=5 and tbp < 8:
	ss += "Duchy"
elif tbp >= 2 and tbp < 5:
	ss += "Estate"

ss += " or " if len(ss)>0 else ""

#treasure cards
if tbp >= 6:
	ss += "Gold"
elif tbp >= 3 and tbp < 6:
	ss += "Silver"
else:
	ss += "Copper"
	
print(ss)

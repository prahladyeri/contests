n = int(input())
p = 0
days = []
for p in range(1, n+1): # these many printers
    st = 0
    for i in range(0, n): # simulate the days
        if i>=(p-1):
            st += p # print statue
        else:
            pass # print printer
        if st >= n: break
    #print('p:st:i:',p,st, i)
    days.append(i+1)
#print("days:", days) 
print(min(days))           
    
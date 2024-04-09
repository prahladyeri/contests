import math

n = int(input())
# if n == 1:
    # print(1)
    # exit()
min_days = 999
for p in range(1, n+1): # these many printing days
    #pp = 1 # no. of printers
    #print('p:', p)
    pp = 2 ** (p-1) # total printers created
    #print('pp:', pp)
    st = math.ceil(n/pp) # no. of days to create statues
    tot_days = st + p -1
    #print("p:pp:st:tot_days", p, pp, st, tot_days)
    if tot_days <= min_days: min_days = tot_days

print(min_days)

"""
n=1
p=1     1       =1 printers (2^0)       = 1/1 = 1 days

n= 5  (4)
p= 1	1,1,1,1,1   =1 printer(2**0)    =5/1 = 5 days
p=2		0,2,2,2
p=3		0,0,4,4

n=7   (4)
p=1		1,1,1,1,1,1,1   =1 printer (2^0)    = 7 / 1 =7 days
p=2		0,2,2,2,2       =2 printers (2^1)
p=3		0,0,3,3,3
p=4		0,0,0,4,4       =8 printers (2^3)   =7/8    =1 days
p=5		0,0,0,0,5,5     =16 printers  (2^4)  =7/16    =1 day
p=6		0,0,0,0,0,6,6       =32 printers (2^4)
p=7		0,0,0,0,0,0,7

n=6 (4)
p=1		1,1,1,1,1,1
p=2		0,2,2,2
p=3		0,0,3,3
p=4		0,0,0,4,4
p=5		0,0,0,0,5,5
p=6		0,0,0,0,0,6
"""
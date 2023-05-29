# test case:
# 1
# 999900000 1000000000

def print_primes_soe(a, n):
    primes= [2,3,5,7] # ,11,13
    m = 2 if a<=2 else a
    #li = list(range(m, n+1))
    #li = [i for i in range(m, n+1)]
    #li = list(range(n+1))
    #li = [i for i in range(n+1)]
    li = dict.fromkeys(range(m, n+1))
    #li[0], li[1] = None, None
    #print("li: ", li)
    for p in primes:
        for i in range(2, n+1):
            s = p*i
            if s>n: break
            #if s in li: li.remove(s)
            #try: li.remove(s)
            #except: pass
            if s>=a: li[s] = 'c'
    #print("li:", li)
    for i in range(m, len(li)):
        if li[i] != 'c': print(i) # and li[i]>=a

n = int(input())
for i in range(n):
    x, y = input().split(' ')
    x, y = int(x), int(y)
    print_primes_soe(x, y)


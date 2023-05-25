def is_prime(j):
    if j<=1: return False
    if j==2: return True
    for k in range(2, j):
        if j%k == 0: return False
    return True
    


n = int(input())
for i in range(n):
    x, y = input().split(' ')
    x, y = int(x), int(y)
    for j in range(x, y+1):
        #if is_prime(j): print(j)
        if j<=1: 
            continue
        elif j==2: 
            print(j)
        else:
            pm = True
            for k in range(2, j):
                if j%k == 0: 
                    pm = False
                    break
            if pm: print(j)
    print("")

if __name__ == "__main__":
    main()
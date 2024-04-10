while(True):
    try:
        vals = input().split()
        if len(vals) !=2: break
        a, b = int(vals[0]), int(vals[1])
        print(abs(a - b))
    except EOFError:
        break

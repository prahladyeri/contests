line = input()
out = []
sout = ""
idx, n = 0, 0
for c in line:
    if c == 'L':
        # idx -= 1
        # if idx<0: idx = 0
        idx = 0 if idx <= 0 else idx - 1
    elif c == 'R':
        # idx += 1
        # if idx>len(out): idx = len(out)
        idx = n if idx >= n else idx + 1
    elif c == 'B' and idx > 0:
        idx -= 1
        #out.pop(idx)
        sout = ''.join([ sout[:idx], sout[idx+1:] ])
        n -= 1
    else:
        #out.insert(idx, c)
        sout = ''.join([sout[:idx] , c , sout[idx:] ])
        n += 1
        idx += 1

#print("".join(out))
print(sout)
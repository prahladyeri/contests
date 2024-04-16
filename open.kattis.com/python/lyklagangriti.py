# import random
# line = ""
# for i in range(1000000):
    # dice = random.randint(0,1)
    # if dice:
        # dice = chr(random.randint(0,2))
        # if dice == 0:
            # line += "L"
        # elif dice == 1:
            # line += "R"
        # elif dice == 2:
            # line += "B"
    # else:
        # line += chr(random.randint(97,122))

line = input()
out = []
idx = 0
#print('now processing..')
for c in line:
# for i in range(len(line)):
    # c = line[i:i+1]
    if c == 'L':
        idx -= 1
        if idx<0: idx = 0
    elif c == 'R':
        idx += 1
        if idx>len(out): idx = len(out)
    elif c == 'B':
        if idx>0: 
            idx -= 1
            out.pop(idx)
            #out = out[:idx] + out[idx+1:]
    else:
        out.insert(idx, c)
        #out = out[:idx] + c + out[idx:]
        idx+=1
    #print(idx, out)
#print('done processing..')
#print('printed', ''.join(out)[:20])
print(''.join(out))
#print(out)
#print(len(out))
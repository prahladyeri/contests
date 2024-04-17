from collections import deque

l, r = deque(), deque()
idx, n = 0, 0
for c in input():
    if c == 'L':
        item = l.pop()
        r.appendleft(item)
    elif c == 'R':
        item = r.popleft()
        l.append(item)
    elif c == 'B':
        l.pop()
    else:
        l.append(c)

print("".join(l) + "".join(r))
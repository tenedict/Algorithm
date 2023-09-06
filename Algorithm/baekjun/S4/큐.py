from collections import deque
import sys

li = []
li = deque(li)

for _ in range(int(sys.stdin.readline())):
    n = list(sys.stdin.readline().split())
    x = n[0]
    if x == 'push':
        li.append(n[1])
    elif x == 'pop':
        if li:
            s = li.popleft()
            print(s)
        else:
            print(-1)
    elif x == 'size':
        print(len(li))
    elif x == 'empty':
        if li:
            print(0)
        else:
            print(1)
    elif x == 'front':
        if li:
            print(li[0])
        else:
            print(-1)
    elif x == 'back':
        if li:
            print(li[-1])
        else:
            print(-1)

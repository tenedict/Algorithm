from collections import deque
n, m = map(int,input().split())

k = int(input())
now = []
for i in range(1,m+1):
    now.append(i)
g = 0
li = [ False for __ in range(n+1)]
now = deque(now)

for noww in now:
    li[noww] = True

for _ in range(k):
    s = int(input())
    yes = False
    while not yes:

        if li[s] == True:
            yes = True
        else:
            if s > max(now):
                g += 1
                po = now.popleft()
                li[po] = False
                now.append(po+m)
                li[po+m] = True
            else:
                g += 1
                po = now.pop()
                li[po] = False
                now.appendleft(po-m)
                li[po-m] = True

print(g)
from collections import deque

n = int(input())
me, you = map(int,input().split())
s = int(input())
li = [[] for _ in range(n+1)]
visited = [False for __ in range(n+1)]
for i in range(s):
    one, two = map(int, input().split())
    li[one].append(two)
    li[two].append(one)

now = [me]
now = deque(now)

success = False
cnt = 0

seq = [0 for _ in range(n+1)]


# print(seq)
while now:
    j = now.popleft()
    if visited[j] == False:
        visited[j] = True
        # print(visited)
        for jj in li[j]:
            now.append(jj)
            seq[jj] = seq[j] + 1
            if jj == you:
                success = True
                break
    if success == True:
        break
if seq[you]== 0:
    print(-1)
else:
    print(seq[you])
    #깃풀실험
            
            

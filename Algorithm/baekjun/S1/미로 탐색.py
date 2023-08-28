from collections import deque
import pprint

n, m = map(int,input().split())

li = []
for _ in range(n):
    line = list(input())
    li.append(line)

visited = [[False for _ in range(m)] for __ in range(n)]

visited[0][0] = True
li[0][0] = 1
now= [[0,0]]
now = deque(now)

while now:
    no = now.popleft()
    if no[0]+1 < m and visited[no[1]][no[0]+1] == False and li[no[1]][no[0]+1] == '1':
        visited[no[1]][no[0]+1] =  True
        li[no[1]][no[0]+1] = li[no[1]][no[0]] + 1
        now.append([no[0]+1,no[1]])
    if no[0] > 0 and visited[no[1]][no[0]-1] == False and li[no[1]][no[0]-1] == '1':
        visited[no[1]][no[0]-1] =  True
        li[no[1]][no[0]-1] = li[no[1]][no[0]] + 1
        now.append([no[0]-1,no[1]])
    if no[1]+1 < n and visited[no[1]+1][no[0]] == False and li[no[1]+1][no[0]] == '1':
        visited[no[1]+1][no[0]] =  True
        li[no[1]+1][no[0]] = li[no[1]][no[0]] + 1
        now.append([no[0],no[1]+1])
    if no[1] > 0 and visited[no[1]-1][no[0]] == False and li[no[1]-1][no[0]] == '1':
        visited[no[1]-1][no[0]] =  True
        li[no[1]-1][no[0]] = li[no[1]][no[0]] + 1
        now.append([no[0],no[1]-1])

print(li[n-1][m-1])
import pprint
from collections import deque
n = int(input())
li = []
for _ in range(n):
    li.append(list(input()))
visited = [[False for _ in range(n)] for _ in range(n)]
realanswer = []


def dfs(y,x,li,visited,n):
    answer = 1
    now = [[x,y]]
    now = deque(now)
    visited[y][x] = True
    while len(now) != 0:
        i = now.popleft()
        #오른쪽
        if i[0] < n-1:
            if li[i[1]][i[0]+1] == '1' and visited[i[1]][i[0]+1] == False:
                now.append([i[0]+1,i[1]])
                visited[i[1]][i[0]+1] = True
                answer += 1
        #아래쪽
        if i[1] < n-1:
            if li[i[1]+1][i[0]] == '1' and visited[i[1]+1][i[0]] == False:
                now.append([i[0],i[1]+1])
                visited[i[1]+1][i[0]] = True
                answer += 1
        #왼쪽
        if i[0] > 0:
            if li[i[1]][i[0]-1] == '1' and visited[i[1]][i[0]-1] == False:
                now.append([i[0]-1,i[1]])
                visited[i[1]][i[0]-1] = True
                answer += 1
        #위쪽
        if i[1] > 0:
            if li[i[1]-1][i[0]] == '1' and visited[i[1]-1][i[0]] == False:
                now.append([i[0],i[1]-1])
                visited[i[1]-1][i[0]] = True
                answer += 1
    realanswer.append(answer)
    answer = 0



for y in range(n):
    for x in range(n):
        if li[y][x] == '1' and visited[y][x] == False:
            dfs(y,x,li,visited,n)
print(len(realanswer))
realanswer.sort()
for ans in realanswer:
    print(ans)
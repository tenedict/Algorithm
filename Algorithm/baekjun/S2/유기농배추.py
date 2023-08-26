from collections import deque
import pprint, sys
n = int(sys.stdin.readline())
for i in range(n):
    g,s,m = map(int,sys.stdin.readline().split())
    bat = [[0]* g for __ in range(s)]
    visited = [[False]* g for __ in range(s)]

    for i in range(m):
        bx,by = map(int,sys.stdin.readline().split())
        bat[by][bx] = 1
    now = []

    cnt = 0
    for y in range(s):
        for x in range(g):
            if bat[y][x] == 1 and not visited[y][x]:
                cnt += 1
                now.append([x,y])
                now = deque(now)
                while now:
                    nn = now.popleft()
                    if nn[0]+1 < g:
                        if bat[nn[1]][nn[0]+1] == 1 and not visited[nn[1]][nn[0]+1]:
                            now.append([nn[0]+1,nn[1]])
                            visited[nn[1]][nn[0]+1] = True
                    if nn[1]+1 <s:        
                        if bat[nn[1]+1][nn[0]] == 1 and not visited[nn[1]+1][nn[0]]:
                            now.append([nn[0],nn[1]+1])
                            visited[nn[1]+1][nn[0]] = True
                    if nn[0] > 0:
                        if bat[nn[1]][nn[0]-1] == 1 and not visited[nn[1]][nn[0]-1]:
                            now.append([nn[0]-1,nn[1]])
                            visited[nn[1]][nn[0]-1] = True
                    if nn[1] > 0:
                        if bat[nn[1]-1][nn[0]] == 1 and not visited[nn[1]-1][nn[0]]:
                            now.append([nn[0],nn[1]-1])
                            visited[nn[1]-1][nn[0]] = True
            if cnt >= m:
                break
    print(cnt)
        
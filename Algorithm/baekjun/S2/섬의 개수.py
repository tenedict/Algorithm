from collections import deque
import pprint
finish = []

while finish != [0,0]:
    finish = list(map(int,input().split()))
    li = []
    for f in range(finish[1]):
        li.append(list(map(int,input().split())))
    
    visited = [[False for _ in range(finish[0])] for __ in range(finish[1])] 
    answer = 0

    for i in range(finish[1]):
        for j in range(finish[0]):
            if li[i][j] == 1 and visited[i][j] == False:
                answer += 1
                now = [[j,i]]
                print(now)
                now = deque(now)
                pprint.pprint(visited)
                while now:
                    n = now.popleft()
                    if n[0] > 0:
                        if  li[n[1]][n[0]-1] == 1 and not visited[n[1]][n[0]-1]:
                            visited[n[1]][n[0]-1] = True
                            now.append([n[0]-1,n[1]])
                            print(111)
                                
                    if n[0]+1 < finish[0]:  
                        if li[n[1]][n[0]+1] == 1 and not visited[n[1]][n[0]+1]:
                            visited[n[1]][n[0]+1] = True
                            now.append([n[0]+1,n[1]])
                            print(222)
                    
                    if n[1]+1 < finish[1]:
                        if li[n[1]+1][n[0]] == 1 and not visited[n[1]+1][n[0]]:
                            visited[n[1]+1][n[0]] = True
                            now.append([n[0],n[1]+1])
                            print(333)

                    if n[1] > 0:
                        if li[n[1]-1][n[0]] == 1 and not visited[n[1]-1][n[0]]:
                            visited[n[1]-1][n[0]] = True
                            now.append([n[0],n[1]-1])
                            print(444)

                    # 대각선
                    if n[0] > 0 and n[1]+1 < finish[1]:
                        if li[n[1]+1][n[0]-1] == 1 and not visited[n[1]+1][n[0]-1]:
                            visited[n[1]+1][n[0]-1] = True
                            now.append([n[0]-1,n[1]+1])
                            print(555)
                    if n[0] > 0 and  n[1] > 0:
                        if li[n[1]-1][n[0]-1] == 1 and not visited[n[1]-1][n[0]-1]:
                            visited[n[1]-1][n[0]-1] = True
                            now.append([n[0]-1,n[1]-1])
                            print(666)
                    if n[0]+1 < finish[0] and n[1]+1 < finish[1]:
                        if li[n[1]+1][n[0]+1] == 1 and not visited[n[1]+1][n[0]+1]:
                            visited[n[1]+1][n[0]+1] = True
                            now.append([n[0]+1,n[1]+1])
                            print(777)
                    if n[0]+1 < finish[0]  and n[1] > 0: 
                        if li[n[1]-1][n[0]+1] == 1 and not visited[n[1]-1][n[0]+1]:
                            visited[n[1]-1][n[0]+1] = True
                            now.append([n[0]+1,n[1]-1])
                            print(888)
    if finish[0] != 0 and finish[1] != 0:
        print('답',answer)
from collections import deque

n, m, s = map(int, input().split())


li=[[] for __ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)
    li[a].sort()
    li[b].sort()

answer1 = [s]
answer2 = []
#dfs
now = s
def dfs(li,now,visited):
    visited[now] = True
    for i in li[now]:
        if visited[i] == False:
            answer1.append(i)
            now = i
            dfs(li,now,visited)



# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        answer2.append(v)
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for k in graph[v]:
            if not visited[k]:
                queue.append(k)
                visited[k] = True




visited = [False]*(n+1)
dfs(li,now,visited)
for __ in answer1:
    print(__,end=' ')

print('')
visited = [False]*(n+1)
bfs(li,s,visited)

for ___ in answer2:
    print(___,end=' ')


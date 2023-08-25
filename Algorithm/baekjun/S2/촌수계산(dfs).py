n = int(input())
me, you = map(int,input().split())
s = int(input())
li = [[] for _ in range(n+1)]
visited = [False for __ in range(n+1)]
for i in range(s):
    one, two = map(int, input().split())
    li[one].append(two)
    li[two].append(one)

now = me
cnt = 0
answer = []
def dfs(li,now,visited,cnt,you,answer):
        cnt += 1
        visited[now] = True
        for i in li[now]:
            if visited[i] == False:
                now = i
                if now == you:
                    answer.append(cnt)
                dfs(li,now,visited,cnt,you,answer)

dfs(li,now,visited,cnt,you,answer)

if answer:
     print(answer[0])
else:
     print(-1)

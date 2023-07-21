from collections import deque
n, k = map(int, input().split())

li= []
for i in range(1,n+1):
    li.append(i)
li = deque(li)
answer = '<'
c = 0
while li:
    c += 1
    if c%k == 0:
        s = li.popleft()
        answer += f'{s}, '
    else:
        s = li.popleft()
        li.append(s)
answer = answer[:-2] + '>' 
print(answer)


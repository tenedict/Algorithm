from heapq import heappush, heappop

n = int(input())
li = []
for i in range(n):
    s = int(input())
    if s != 0:
        heappush(li,-s)
    else:
        if len(li) != 0:
            print(-heappop(li))
        else:
            print(0)



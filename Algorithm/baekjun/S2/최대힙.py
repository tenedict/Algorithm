from heapq import heappush, heappop
import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
    s = int(sys.stdin.readline())
    if s != 0:
        heappush(li,-s)
    else:
        if len(li) != 0:
            print(-heappop(li))
        else:
            print(0)
# sys안쓰고 할라면 어케해야할까 ㅜ



# n,m = map(int, input().split())
# li = list(map(int, input().split()))



# for k in range(m):
#     inli = []
#     i,j= map(int, input().split())
#     answer = 0
#     for l in range(j-i+1):
#         answer +=  (li[i-1+l])
#     print(answer)
# 시간 초과됨

# n,m = map(int, input().split())
# li = list(map(int, input().split()))

# for k in range(m):
#     i, j = map(int, input().split())
#     answer = 0
#     h = i
#     while h <= j:
#         answer += li[h-1]
#         h = h + 1
#     print(answer)

n,m = map(int, input().split())
li = list(map(int, input().split()))
for k in range(1,n):
        li[k] += li[k-1]
li = [0] + li
for u in range(m):
    i, j = map(int, input().split())
    print(li[j]-li[i-1])

# 4860ms 126436kb 시간 줄여봐야겠다.


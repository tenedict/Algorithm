n, m = map(int, input().split())
li = list(map(int, input().split()))

# realanswer = 0

# answer = 0

# for i in range(n-m+1):
#     answer = 0
#     for j in range(m):
#         answer += li[i+j]
#     if answer > realanswer:
#         realanswer = answer
# print(realanswer)

li1 = []
li1.append(0)
c = 0
g = True
realanswer = 0
for i in li:
    c += i
    li1.append(c)
for j in range(m,n+1):
    answer = li1[j]-li1[j-m]
    print(answer)
    if realanswer < answer or g == True:
        realanswer = answer
        g = False
print(realanswer)

# 처음에는 리스트 인덱스를 돌며 계산했지만 시간초과가 생겨 누적합이라는 힌트를 얻어서 푸는데 성공했다!
    
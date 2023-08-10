t, n = map(int,input().split())

a = t//n

answer = 0
for i in range(a+1):
    b = t-(n*i)
    #b의 개수
    #i는 a의 개수
    apack = 1
    bpack = 1
    allpack = 1
    for asu in range(1,i+1):
        apack = apack*asu
    for bsu in range(1,b+1):
        bpack = bpack*bsu
    for allsu in range(1,i+b+1):
        allpack = allpack*allsu
    answer += (allpack)//(apack*bpack)

print(answer%1000000007)
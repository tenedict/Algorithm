n = int(input())
li = list(map(int, input().split()))
m = int(input())
li.sort()

b =0
a = 0

for i in range(n):
    if li[i] > m:
        b = li[i]
        if i >0:
            a = li[i-1]
            break
        else:
            a = 0
            break




lista = []
t = True
while t:
    a += 1
    if m >=a:
        lista.append(a)
    else:
        t = False

listb = []
f = True
while f:
    b -= 1
    if m <= b:
        listb.append(b)
    else:
        f = False

# if not lista:
#     for k in range(1,m):
#         lista.append(k)

answer = 0
for i in lista:
    for j in listb:
        if j>i:
            answer += 1
        else:
            continue
print(answer)


#기차에서 풀다가 틀렸는데 멀미나서 생각하기가 싫음
# 다음날 풀었다 !! 반례가 짜증나는군!!



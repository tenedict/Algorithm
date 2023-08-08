n = int(input())
vip = []
for _ in range(int(input())):
    vip.append(int(input()))

su = []
cnt = 0
for i in range(1,n+1):
    if i in vip:
        if cnt != 0:
            su.append(cnt)
            cnt = 0
    elif i == n:
        cnt += 1
        su.append(cnt)
    else:
        cnt += 1


su.sort()
if su:
    pibo = [1,2]
    while len(pibo) < su[-1]:
        pibo.append(pibo[-1]+pibo[-2])


    answer = 1
    for s in su:
        answer = answer*pibo[s-1]

    print(answer)
else:
    print(1)
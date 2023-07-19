n = int(input())

li = []

# 강의실 사람 배치
for i in range(n):
    inli = list(map(int, input().split()))
    li.append(inli)


gyosu = []
me = []
alljomuregi = []

x = -1
for j in li:
    x += 1
    y = -1
    for jj in j:
        y += 1
        if jj == 5:
            gyosu.append(x)
            gyosu.append(y)
        elif jj == 2:
            me.append(x)
            me.append(y)
        elif jj == 1:
            jomuregi = []
            jomuregi.append(x)
            jomuregi.append(y)
            alljomuregi.append(jomuregi)
        else:
            continue
squx = []
squy = []
squx.append(gyosu[0])
squx.append(me[0])
squy.append(gyosu[1])
squy.append(me[1])

squx.sort()
squy.sort()
yes = True
# 교수랑 나 거리 확인
if (gyosu[0]-me[0])**2+(gyosu[1]-me[1])**2 >= 25:
    jomusu = 0
    for k in alljomuregi:
        # 조무래기가 사이에 있는가
        if k[0] >= squx[0]and k[0] <= squx[1]:
            if k[1] >= squy[0]and k[1] <= squy[1]:
                jomusu += 1
                if jomusu == 3:
                    print(1)
                    yes = False

if yes:
    print(0)



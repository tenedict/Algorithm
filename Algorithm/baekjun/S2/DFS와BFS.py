n, m, s = map(int, input().split())

li = []
for i in range(n):
    smallli = []
    li.append(smallli)

for j in range(m):
    st, en = map(int,input().split())
    li[st-1].append(en)

visit = []
visit.append(s)
for k in range(len(li)):
    for kk in range(len(li[k])):
        if li[k][kk] not in visit:
            visit.append(li[k][kk])
        elif len(visit) == n:
            print(visit)
            break
    if len(visit) == n:
        print(visit)
        break
    # 실패
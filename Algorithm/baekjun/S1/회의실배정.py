n = int(input())

li = []

for _ in range(n):
    li.append(list(map(int,input().split())))
li.sort(key=lambda x:x[1])
now = 0
answer = 0

im = []
for i in li:
    if not im or im[0][1] == i[1]:
        im.append(i)

    else:
        im.sort(key=lambda x:x[0])
        for j in im:
            if j[0] >= now:
                answer += 1
                now = j[1]
                im = []
            else:
                im = []
        im.append(i)

im.sort(key=lambda x:x[0])
for j in im:
    if j[0] >= now:
        answer += 1
        now = j[1]
        im = []


print(answer)
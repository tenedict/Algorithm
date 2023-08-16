s, n = map(int,input().split())
li = []

j = s//n
na = s%n

for i in range(n):
    li.append(j)    

while na != 0:
    for k in range(n):
        if na != 0:
            li[k] += 1
            na -= 1
        else:
            break

answer = 1
for ii in li:
    answer *= ii

print(answer)








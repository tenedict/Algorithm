
um = []
yang = []
il = []
yong = []

for _ in range(int(input())):
    inp = int(input())
    if inp < 0:
        um.append(inp)
    elif inp == 1:
        il.append(inp)
    elif inp >0:
        yang.append(inp)
    else:
        yong.append(inp)

answer = 0

yang.sort()
um.sort(reverse=True)


while len(yang) > 1:
    a = yang.pop()
    b = yang.pop()
    answer += (a*b)

if yang:
    answer += yang[0]

while len(um) > 1:
    a = um.pop()
    b = um.pop()
    answer += (a*b)
if um:
    if not yong:
        answer += um[0]

answer += len(il)
print(answer)

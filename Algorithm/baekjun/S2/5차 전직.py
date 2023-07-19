n, k = map(int, input().split())

quest = list(map(int, input().split()))

quest.sort()
print(quest)

akane = 0
routine = -1

for i in quest:
    routine += 1
    if routine < k:
        akane += i*routine
    elif routine >= k:
        akane += i*k
    else:
        continue

print(akane)
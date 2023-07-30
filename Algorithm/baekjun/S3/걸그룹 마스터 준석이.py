n,m = map(int, input().split())

group = {}

for i in range(n):
    groupname = input()
    girls = []
    for j in range(int(input())):
        girls.append(input())
    group[groupname] = girls

# print(group)
for _ in range(m):
    answer = input()
    what = int(input())
    if what == 0:
        ga = group[answer]
        ga = list(ga)
        ga.sort()
        for __ in ga:
        
            print(__)
    else:
        cnt = 0
        for ___ in group.values():
            if answer in ___:
                print(list(group.keys())[cnt])
            cnt += 1


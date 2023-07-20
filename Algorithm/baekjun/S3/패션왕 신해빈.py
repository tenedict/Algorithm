n = int(input())

for _ in range(n):
    dress = {}
    for __ in range(int(input())):
        name, kind = input().split()
        if kind in dress:
            dress[kind] += 1
        else:
            dress[kind] = 1
    answer = 1
    for i in dress.values():
        answer = answer*(i+1)
    print(answer-1)

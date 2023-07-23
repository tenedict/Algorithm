import sys
n = int(sys.stdin.readline())
people = {}
for i in range(n):
    s = sys.stdin.readline()
    if s not in people:
        people[s] = 1
    else:
        people[s] += 1


for j in range(n-1):
    ss = sys.stdin.readline()
    people[ss] -= 1

for k in people:
    a = people.get(k)
    if a == 1:
        print(k)

# 인풋 안쓰고 시간초과 안날라면어케해야해;;
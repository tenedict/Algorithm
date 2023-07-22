n = input()
li = []
answer = ''
for i in n:
    li.append(ord(i))

for j in range(97,123):
    s = li.count(j)
    answer += f'{s} '

print(answer)

n = int(input())

li = [1,1]

if n != 1:
    while len(li) != n+1:
        li.append(li[-1]+li[-2])


print(li[-1]%10007)
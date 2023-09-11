n = int(input())

yes = 0
cnt = 0

while yes == 0:
    if n%5 != 0:
        if n >= 3:
            n -= 3
            cnt += 1
        else:
            yes = 2
    else:
        cnt += n//5
        yes = 1

if yes == 1:
    print(cnt)
else:
    print(-1)
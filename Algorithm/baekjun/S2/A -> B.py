n, m = map(int,input().split())

mm = str(m)

yes = True
impossible = False
count = 1

while yes:
    if m == n:
        yes = False
        impossible = False
        break
    if m < n:
        yes = False
        impossible = True

    elif mm[-1] == '1':
        count += 1
        mm = mm[:-1]
        m = int(mm)
        print(m)

    elif m%2 == 0:
        count += 1
        m = round(m/2)
        mm = str(m)
        print(m)

    else:
        yes = False
        impossible = True

if impossible:
    print(-1)
else:
    print(count)
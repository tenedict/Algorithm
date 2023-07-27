n = int(input())
li = list(map(int, input().split()))
m = int(input())
li.sort()

b =0
a = 0

for i in range(n):
    if li[i] > m:
        b = li[i]
        if i >= 1:
            a = li[i-1]
            break

cnt1 = 0
t = True
while t:
    a += 1
    if m >=a:
        cnt1 += 1
    else:
        t = False
cnt2 = 0
f = True
while f:
    b -= 1
    if m <= b:
        cnt2 += 1
    else:
        f = False

if (cnt1*cnt2-1) >0:
    print(cnt1*cnt2-1)
else:
    print(0)



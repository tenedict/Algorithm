n = int(input())
s = int(input())

n = str(n)

n = list(n)
n[-2] = '0'
n[-1] = '0'
ss = ''
for i in n:
    ss += i

ss = int(ss)

game = True

while game:
    if ss%s == 0:
        ans = str(ss)[-2:]
        print(format(ans, '02'))
        game =False
    else:
        ss += 1


        
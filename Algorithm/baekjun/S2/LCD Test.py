s, m = map(int, input().split())
m = str(m)
mm = []
for ii in m:
    mm.append(int(ii))
m = mm

sero = 2*s + 3


for cnt in range(1,sero+1):
    ma = ''
    # 탑
    if cnt == 1:
        for top in m:
            if top in [2,3,5,6,7,8,9,0]:
                ma += ' '
                ma += '-'*s
                ma += ' '
            else:
                ma += ' '
                ma += ' '*s
                ma += ' '
            ma += ' '
    # 바론
    elif cnt >1 and cnt <= sero//2:
        for baron in m:
            if baron in [1,2,3,7]:
                ma += ' '*(s+1)
                ma += '|'
            elif baron in [4,8,9,0]:
                ma += '|'
                ma += ' '*s
                ma += '|'

            else:
                ma += '|'
                ma += ' '*(s+1)
            ma += ' '
    # 미드
    elif sero//2 +1 == cnt:
        for mid in m:
            if mid in [2,3,4,5,6,8,9]:
                ma += ' '
                ma += '-'*s
                ma += ' '
            else:
                ma += ' '*(s+2)
            ma += ' '
               
    # 드래곤
    elif cnt < sero and sero//2+1 < cnt:
        for dragon in m:
            if dragon in [1,3,4,5,7,9]:
                ma += ' '*(s+1)
                ma += '|'


            elif dragon in [2]:
                ma += '|'
                ma += ' '*(s+1)
              
            else:
                ma += '|'
                ma += ' '*s
                ma += '|'
            ma += ' '
    # 바텀
    if cnt == sero:
        for bot in m:
            if bot in [2,3,5,6,8,9,0]:
                ma += ' '
                ma += '-'*s
                ma += ' '
            else:
                ma += ' '
                ma += ' '*s
                ma += ' '
            ma += ' '
    
    print(ma)
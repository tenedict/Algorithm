n = int(input())

li = ['0','1','2','3','4','5','6','7','8','9',' ']
cnt = 0
while cnt == n:
    s = ''
    for i0 in li:
        s += i0
        for i1 in li:
            if i0 > i1:
                s += i1
                for i2 in li:
                    if i0 > i1:
                        s += i1
                        for i3 in li :
                            if i0 > i1:
                                s += i1
                                for i4 in li:
                                    if  i0 > i1:
                                        s += i1
                                        for i5 in li:
                                            if i0 > i1:
                                                s += i1
                                                for i6 in li:
                                                    if i0 > i1:
                                                        s += i1
                                                        for i7 in li:
                                                            if i0 > i1:
                                                                s += i1
                                                                for i8 in li:
                                                                    if i0 > i1:
                                                                        s += i1
                                                                        for i9 in li:
                                                                            if i0 == 0 or i0 > i1:
                                                                                s += i1

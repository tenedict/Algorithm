word = input()
n, m = map(int,input().split())
box = []
for _ in range(m):
    box.append(list(input()))

success = False

#가로 찾기
for j in range(m):
    if success:
        break
    else:
        for i in range(n):
            if success:
                break
            else:
                for way in range(8):    
                    
                    g = i
                    rg = i
                    s = j
                    rs = j
                    rug = i
                    rus = j
                    lug = i
                    lus = j
                    rdg = i
                    rds = j
                    ldg = i
                    lds = j
                    if way == 0:
                        cnt = 0
                        for k in word:
                            if box[j][g] == k:
                                cnt += 1
                                if cnt == len(word):
                                    success = True
                                    break
                                if g+1 < n:
                                    g += 1
                                else:
                                    break
                            else:
                                break
                    if way == 1:
                        cnt = 0
                        for k in word:
                            if box[j][rg] == k:
                                cnt += 1
                                if cnt == len(word):
                                    success = True
                                    break
                                if rg-1 > -1:
                                    rg -= 1
                                else:
                                    break
                            else:
                                break
                    if way == 2:
                        cnt = 0
                        for k in word:
                            if box[s][i] == k:
                                cnt += 1
                                if cnt == len(word):
                                    success = True
                                    break
                                if s+1 < m:
                                    s += 1
                                else:
                                    break
                            else:
                                break

                    if way == 3:
                        cnt = 0
                        for k in word:
                            if box[rs][i] == k:
                                cnt += 1
                                if cnt == len(word):
                                    success = True
                                    break
                                if rs-1 > -1:
                                    rs -= 1
                                else:
                                    break
                            else:
                                break
                    if way == 4:
                        cnt = 0
                        for k in word:
                            if box[rus][rug] == k:
                                cnt += 1
                                if cnt == len(word):
                                    success = True
                                    break
                                if rug+1 < n and rus-1 > -1:
                                    rug += 1
                                    rus -= 1
                                else:
                                    break
                            else:
                                break
                    if way == 5:
                        cnt = 0
                        for k in word:
                            if box[lus][lug] == k:
                                cnt += 1
                                if cnt == len(word):
                                    success = True
                                    break
                                if lug-1 > -1 and lus-1 > -1:
                                    lug -= 1
                                    lus -= 1
                                else:
                                    break
                            else:
                                break
                    if way == 6:
                        cnt = 0
                        for k in word:
                            if box[rds][rdg] == k:
                                cnt += 1
                                if cnt == len(word):
                                    success = True
                                    break
                                if rdg+1 < n and rds+1 <m:
                                    rdg += 1
                                    rds += 1
                                else:
                                    break
                            else:
                                break
                    if way == 7:
                        cnt = 0
                        for k in word:
                            if box[lds][ldg] == k:
                                cnt += 1
                                if cnt == len(word):
                                    success = True
                                    break
                                if lds+1 < m and ldg > -1:
                                    lds += 1
                                    ldg -= 1
                                else:
                                    break
                            else:
                                break


    
            
print(int(success))
                
                
        

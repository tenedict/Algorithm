n, m = map(int, input().split())

sixprice = 0
oneprice = 0
cnt = 0

for i in range(m):
    
    sixpack, one = map(int, input().split())
    if cnt > 0:
        if sixpack < sixprice:
            sixprice = sixpack
        
        if oneprice > one:
            oneprice = one
    else:
        sixprice = sixpack
        oneprice = one
        cnt += 1

    
print(sixprice, oneprice)
j = n//6
k = n%6

answer1 = sixprice*j + k*oneprice
answer2 = n*oneprice
if k != 0:
    answer3 = sixprice*(j+1)
else:
    answer3 = sixprice*j
li = [answer1, answer2, answer3]
li.sort()
print(li[0])
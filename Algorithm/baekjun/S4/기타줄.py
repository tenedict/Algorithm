n, m = map(int, input().split())

sixprice = 0
s = False
oneprice = 0
o = False

for i in range(m):
    sixpack, one = map(int, input().split())
    print(oneprice,'kkkkklllll')
    if sixpack < sixprice and s == True:
        sixprice = sixpack
    else: 
        sixprice = sixpack
        s = True
    
    if oneprice > one and o == True:
        oneprice = one
    else:
        oneprice = one
        o = True
    
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
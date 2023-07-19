n,k = map(int, input().split())

li = []
for nn in range(2,n+1):
    li.append(nn)


removeli = []
print(li)

def lii():
    s = li[0]
    for j in li:
        if j%s == 0:
            print(j, 'remove')
            li.remove(j)
            removeli.append(j)
            print(li)
            if len(removeli) == k:
                print(j)
            
while len(removeli) < k:
    lii()
    


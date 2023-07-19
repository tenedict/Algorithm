n,k = map(int, input().split())

li = []
for nn in range(2,n+1):
    li.append(nn)


removeli = []


def lii():
    s = li[0]
    for j in li:
        if j%s == 0:
            li.remove(j)
            removeli.append(j)

            if len(removeli) == k:
                print(j)
            
while len(removeli) < k:
    lii()
    


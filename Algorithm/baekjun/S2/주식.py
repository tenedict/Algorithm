import sys

def tesla():
    n = int(sys.stdin.readline())
    tsla = list(map(int,sys.stdin.readline().split()))
    tsla = list(reversed(tsla))
    profit = 0
    high = tsla[0]
    for i in tsla:
        if i < high:
            profit += (high-i)
        else:
            high = i
    
    print(profit)

for _ in range(int(sys.stdin.readline())):
    tesla()
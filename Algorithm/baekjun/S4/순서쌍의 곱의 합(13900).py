
a = int(input())
li = list(map(int, input().split()))


s = 0
answer = 0

for i in li:
    answer += i * s
    s += i
    
    



print(answer)




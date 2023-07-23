import pprint
from collections import deque
game = True

n = int(input())

board = []
for i in range(n+2):
    li = [0]*(n+2)
    board.append(li)
for ii in range(n+1):
    board[0][ii] = 4
    board[ii][0] = 4
    board[n+1][ii] = 4
    board[ii][n+1] = 4

#시간 계산
time = 0


#뱀의 위치
board[1][1] = 1
headx = 1
heady = 1
tailx = 1
taily = 1
way = 'east'

apples = int(input())

for apple in range(apples):
    #applelocate
    x, y = map(int, input().split())
    board[x][y] = 9


turns = int(input())
turntime = []
turnway = []
turntime = deque(turntime)
turnway = deque(turnway)
for k in range(turns):
    a, b = input().split()
    turntime.append(a)
    turnway.append(b)
eatapple = 0
wayhistory = []
while game == True:
    
    if turntime:
        if int(turntime[0]) == time:
            turntime.popleft()
            leftright = turnway.popleft()
            if leftright == 'L':
                if way == 'east':
                    way = 'north'
                elif way == 'south':
                    way = 'east'
                elif way == 'north':
                    way = 'west'
                elif way == 'west':
                    way = 'south'
            elif leftright == 'D':
                if way == 'east':
                    way = 'south'
                elif way == 'south':
                    way = 'west'
                elif way == 'north':
                    way = 'east'
                elif way == 'west':
                    way = 'north'
    wayhistory.append(way)
    tailway = wayhistory[time-eatapple]



    #뱀 이동
    pprint.pprint(board)
    aaa = 0
    if way == "east":
        headx += 1
        time+=1
        if board[heady][headx] != 4:
            if board[heady][headx] == 9:
                aaa = 1
                eatapple += 1
            board[heady][headx] = 4
        else:
            print(time)
            game = False
            
    elif way == "west":
        headx -= 1
        time+=1
        if board[heady][headx] != 4:
            if board[heady][headx] == 9:
                aaa = 1
                eatapple += 1
            board[heady][headx] = 4
        else:
            print(time)
            game = False

    elif way == "north":
        heady -= 1
        time+=1
        if board[heady][headx] != 4:
            if board[heady][headx] == 9:
                aaa = 1
                eatapple += 1
            board[heady][headx] = 4
        else:
            print(time)
            game = False

    elif way == "south":
        heady += 1
        time+=1
        if board[heady][headx] != 4:
            if board[heady][headx] == 9:
                aaa = 1
                eatapple += 1
            board[heady][headx] = 4
        else:
            print(time)
            game = False
    


    if tailway == "east":
        if aaa == 0:
            tailx += 1
            board[taily][tailx -1] = 0

            
    elif tailway == "west":
        if aaa == 0:
            tailx -= 1
            board[taily][tailx+1] = 0


    elif tailway == "north":
        if aaa == 0:
            taily -= 1
            board[taily+1][tailx ] = 0

    elif tailway == "south":
        if aaa == 0:
            taily += 1
            board[taily-1][tailx] = 0

# 처음푼 골드~~
 

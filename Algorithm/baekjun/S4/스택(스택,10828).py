import sys


a = int(sys.stdin.readline().strip())
list = []

for i in range(a):
    s = sys.stdin.readline().strip()
    print(s, type(s))
    if s == "top":
        if list:
            print(list[-1])
        else:
            print(-1)
    elif s == "size":
        print(len(list))

    elif s == "empty":
        if list:
            print(0)
        else:
            print(1)
    elif s == "pop":
        if list:
            pp = list.pop()
            print(pp)
        else:
            print(-1)

    else:
        list.append(int(s[4:]))
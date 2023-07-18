n = int(input())
one, two = input().split('*')
for i in range(n):
    word = input()
    len1 = len(one)
    len2 = len(two)

    # if len(one+two) <= len(word):
    #     if word[0:len1] == one:
    #         if word[-len2:] == two:
    #             print('DA')
    #         else:
    #             print('NE')    
    #     else:
    #         print('NE')
    # else:
    #     print('NE')
        
    if len(one+two) <= len(word) and word[0:len1] == one and word[-len2:] == two:
        print('DA')
    else:
        print('NE')
        


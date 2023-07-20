# words = input()
# answer = []
# for j in words:
#     code = ord(j)
#     if code >= 65 and code <= 90:
#         code = code + 13
#         if code >= 65 and 90 >= code:
#             answer.append(code)
#         elif code > 90:
#             code = -90+code+ 64
#             answer.append(code)
#     elif code >= 97 and 122 >= code:
#         code = code + 13
#         if code <= 122:
#             answer.append(code)
#         elif code > 122:
#             code = -122+code+96
#             answer.append(code)
#     else:
#         answer.append(code)

# rot13 = ''
# for j in answer:
#     rot13 += chr(j)
# print(rot13)

words = input()
answer = []
for i in words:
    code = ord(i)
    if code >= 65 and code <= 90:
        largecode = (code+13-65)%26
        answer.append(largecode+65)
    elif code >= 97 and code <= 122:
        smallcode = (code-97+13)%26
        answer.append(smallcode+97)
    else:
        answer.append(code)
rot13 = ''
for j in answer:
    rot13 += chr(j)
print(rot13)


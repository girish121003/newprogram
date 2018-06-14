def correcparenthesis(s):
    stack = []
    braces = {'(': ')', '[': ']', '{': '}'}

    for ch in s:
        if ch in braces:
            stack.append(braces[ch])
            continue

        if not stack or ch != stack.pop():
            return False

    return not stack

b= input("Enter the string")
k=correcparenthesis(b)
print(k)


# lis_b=['(',')','{','}','[',']']
# count=0
# countloop=0
# dict_b={'(':')','[':']','{':'}'}
# k=0
# for x in range(len(b)):
#     if b[x] not in lis_b:
#       count=count+1
# if count==0:
#     if b[0]  not in  dict_b.keys():
#         print("Wrong")
#     else:
#
#         if(len(b)%2==0):
#             l=int(len(b)/2)
#             for y in range(l):
#                 if dict_b[b[y]]==b[-1]:
#                     b.pop()
#                     countloop+=1
#
#
# if(countloop==len(b/2)):
#     print(True)
# else:
#     print(False)



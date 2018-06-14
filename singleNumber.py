k=[int(x) for x in input().split()]

a=0

for i in k:
    a=a^i

print(a)
# k.sort()
# dict={}
#
# for y in range(len(k)):
#     count = 1
#     if k[y] not in dict:
#         dict[k[y]]=count
#     else:
#         count=dict[k[y]]
#         count=count+1
#         dict[k[y]]=count
# for m in range(len(k)):
#     if dict[k[m]]==1:
#         print(k[m])
# for m in range(len(dict)):
#     if dict[m]==1:
#         print(k[m])
# while (count<len(k)):
#     if(count+1<=len(k)):
#         if k[count]!=k[count+1] or k[count+1]==k[-1] :
#             print(k[count])
#             count=count+1
#         elif k[count]==k[-1]:
#             print(k[count])
#         else:
#             count=count+2



print("Enter the array containig 0's: ")
arr=[int(x) for x in input().split()]

i=0
j=0
count=0
for i in range(len(arr)):
    if(arr[i]!=0):
        arr[count]=arr[i]
        count=count+1

while(count<len(arr)):
    arr[count]=0
    count=count+1

# while(i<len(arr)):
#     j=i+1
#     k=0
#     while(j<len(arr)):
#         if(arr[i]==0):
#             if(arr[j]==0):
#                 j=j+1
#             else:
#                 k=arr[i]
#                 arr[i]=arr[j]
#                 arr[j]=k
#                 j+=1
#         else :
#                 j=j+1
#     i=i+1

print(arr)
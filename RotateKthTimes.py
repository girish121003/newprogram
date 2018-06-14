nums=[int(x) for x in input().split()]
k=int(input("Enter the number of times you want to rotate the string : "))
if len(nums)==1 or len(nums)==0:
    print(nums)
else:
    temp=0
    nums1=[]
    nums2=[]
    for x in range(len(nums)):
        sum = 0
        sum = x + k+1
        if(sum<len(nums)):
            nums1.append(sum)
        else:
            sum=sum-len(nums)
            nums1.append(sum)
    print(nums1)
    for y in range(len(nums)):
        nums2.append(nums[nums1[y]])
    nums=list(nums2)
    print(nums)
# for x in range(k):
#     temp = nums[-1]
#     for y in range(len(nums)-1,-1,-1):
#         nums[y]=nums[y-1]
#     nums[0]=temp

# print(nums)
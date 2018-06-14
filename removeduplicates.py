def removeDuplicates(nums,value):
    if not nums:
        return 0

    temp=0
    for x in range(len(nums)):
        if(nums[x]!=value):
            nums[temp]=nums[x]
            temp = temp + 1

    return temp





print("Enter the elements")
a=[int(x) for x in input().split()]
k=int(input("Enter The value"))
l=removeDuplicates(a,k)
for x in range(l):
    print(a[x])
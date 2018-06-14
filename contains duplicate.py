def containsDuplicate(nums):
    if(len(nums)>1):
        count=0
        giru=[]
        nums.sort()
        for i in range(len(nums)):
            if i+1<len(nums):
                if(nums[i]==nums[i+1]):
                    count=count+1

        if(count>0):
            return True
        else: return False
    else :
        return False















print("enter the element in an array")
a=[int(x) for x in input().split()]
k=containsDuplicate(a)

print(k)
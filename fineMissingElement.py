def findDisappearedNumbers(nums):
    nums.sort()
    ret = []
    for i in range(len(nums)):
            if(nums[i]-nums[i-1]>1):
                count=nums[i]-nums[i-1]-1
                k=nums[i-1]
                for j in range(count):
                    k+=1
                    ret.append(k)
    return ret

print("enter the element in an array")
a=[int(x) for x in input().split()]
k= findDisappearedNumbers(a)
print(k)

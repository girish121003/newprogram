def twoSum( nums, target):
    if len(nums) <= 1:
        return False
    k = {}
    for i in range(len(nums)):
        if nums[i] in k:
            return [k[nums[i]], i]
        else:
            k[target - nums[i]] = i


print("Enter the element in array")
a=[int(x) for x in input().split() ]
target=int(input("Enter the Target value :"))
x=twoSum(a,target)
print(x)
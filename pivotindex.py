def pivotIndexOptimized(nums):
    if len(nums) <= 2:
        return -1
    left_sum, pivot, right_sum = 0, 0, sum(nums[1:])
    if left_sum == right_sum:
        return pivot
    for i in range(len(nums) - 1):
        left_sum += nums[pivot]
        pivot += 1
        right_sum -= nums[pivot]
        if left_sum == right_sum:
            return pivot
    return -1


print("enter the element in an array")
a=[int(x) for x in input().split()]
k= pivotIndexOptimized(a)
print(k)

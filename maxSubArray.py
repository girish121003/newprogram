def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 1;
    maxi = nums[0]
    listsums = nums[0];
    len1 = len(nums)
    while i < len1:
        if maxi < nums[i]:
            maxi = nums[i]
        if listsums + nums[i] < nums[i]:
            listsums = nums[i]
        else:
            listsums = listsums + nums[i]
        if listsums > maxi:
            maxi = listsums
        i += 1
    return maxi

number=[int(x) for x in input().split()]
m=maxSubArray(number)
print(m)

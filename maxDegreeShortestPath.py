def findShortestSubArray(nums):
    left, right, count = {}, {}, {}
    for i, x in enumerate(nums):
        if x not in left: left[x] = i
        right[x] = i
        count[x] = count.get(x, 0) + 1

    ans = len(nums)
    degree = max(count.values())
    for x in count:
        if count[x] == degree:
            ans = min(ans, right[x] - left[x] + 1)

    return ans

print("enter the element in an array")
a=[int(x) for x in input().split()]
k= findShortestSubArray(a)
print(k)

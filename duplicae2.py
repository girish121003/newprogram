def containsNearbyDuplicate(nums, k):
    h = {}
    for i, num in enumerate(nums):
        if num in h and i - h[num] <= k:
            return True
        h[num] = i
    return False
print("enter the element in an array")
a=[int(x) for x in input().split()]
n=int(input("Enter the number"))
j=containsNearbyDuplicate(a,n)

print(j)
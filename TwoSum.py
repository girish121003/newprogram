
class Solution:
    def twoSum(self, nums, target):
        i=0
        while (i < len(a)):
            j = 0
            while (j < len(a)):
                if (i != j):
                    if (a[i] + a[j] == target):
                        return(i, j)
                j = j + 1
            i = i + 1


print("Enter elements : ")
a = [int(x) for x in input().split()]
target=int(input("Enter the target sum : "))

sol = Solution()
k=sol.twoSum(a,target)
print(k)


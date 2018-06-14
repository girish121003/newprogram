class Solution :
    def searchInsert(self,nums,target):
        i=0
        if(nums[0]>target) :
            return 0
        elif(nums[-1]<target):
            return len(nums)
        else :
            while(i<len(nums)):
                if(nums[i]==target):
                    return i
                elif(nums[i]>target):
                    return i
                i=i+1

print("Enter the numbers: ")
a=[int(x) for x in input().split()]
target=int(input("Enter the number needs to be searched/inserted "))
sol=Solution()
k=sol.findTarget(a,target)
print(k)
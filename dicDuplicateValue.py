from dictionaries import Dict
class solution :
    def function1(self, nums):
        i=0
        if(len(nums)==0): return 0

        for j in range(1,len(nums)):
            if(nums[j]!=nums[i]):
                i=i+1
                nums[i]=nums[j]
            else:
                i=i+1
        return nums
print("Kindly Enter the sorted list of duplicated numbers: ")
a = [int(x) for x in input().split()]
sol=solution()
k=sol.function1(a)
print(k)


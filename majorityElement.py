def getMax(nums):
    if(len(arr)==1):
        return arr[0]
    else:
        i=0

        storemax={}
        nums.sort()
        while(i<len(nums)):
            j=i+1
            counter = 1
            while(j<len(nums)):
                if(nums[i]==nums[j]):
                    counter=counter+1
                    storemax[nums[i]] = counter
                    j=j+1
                else:
                    j=j+1
            i=i+1
    maxnum=max(storemax,key=storemax.get)
    return maxnum


arr=[int(x) for x in input().split()]
num=getMax(arr)
print(num)
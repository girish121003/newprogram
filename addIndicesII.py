'''Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.'''


k=[int(x) for x in input().split()]
target=int(input("Enter the target number"))
storeIndex=[]

start=0
last=len(k)-1

while start<last:
    if k[start]+k[last]>target: # if the target value is greater than the sum of elements, number should be reduces at the end of the list to achieve the target
        last-=1
    elif k[start]+k[last]<target:# if smaller than the sum value from the start should be increased to achieved the sum
        start+=1
    else:
        storeIndex.append(start+1) # storing the first smaller indexe with non -zero value
        storeIndex.append(last+1)# storing the second index
        break


print(storeIndex) # printing the indexes

def sumofpairs(nums):
    nums.sort()
    j=0
    sum=0
    while(j<len(arr)):
        sum=sum+arr[j]
        j=j+2
    return sum

p=int(input("Enter The Elements : "))
n=p/2
arr = []
for i in range(p):
    arr.append(int(input("Enter %d element" % i)))

k=sumofpairs(arr)
print(k)
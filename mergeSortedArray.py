def mergeSortedArray(nums1,nums2, m,n):
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]



a=int(input("Enter the number of elements for the first array"))
numj=[]
for k in range(a):
    l=int(input())
    numj.append(l)
j=[x for x in numj if x!=0]
numj.sort()
b=int(input("Enter the number of element for the second array"))
numk=[]
for y in range(b):
    u=int(input())
    numk.append(u)
v=[y for y in numk if y!=0]
v.sort()
k=mergeSortedArray(numj,numk,a,b)
print(k)



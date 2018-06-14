nums1=[int(x) for x in input().split()]
nums2=[int(y) for y in input().split()]
nums1=nums1+nums2
nums1.sort()
k=len(nums1)
if(len(nums1)==1):
    print(nums1[0])
else:
    median=0.0
    if(len(nums1)%2==0):
        z=int((len(nums1)/2)-1)
        c=int((len(nums1)/2))
        median=float((nums1[z]+nums1[(c)])/2)
    else:
        median=float(nums1[int((len(nums1)+1)/2)-1])
    print(median)
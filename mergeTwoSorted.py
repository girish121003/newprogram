class Solution:
    def sortList(self,nums1,nums2,m,n):
        if(m==0):
            nums1=list(nums2)
            return nums1
        elif(n==0):
            return nums1

        elif(m==1 and n==1):
         nums1.append(nums2[0])
         return  nums1
        else:
            i=0
            k=m+n
            while(m<k and i<n):
                nums1.append(nums2[i])
                i=i+1
                m=m+1
        nums1.sort()
        return nums1

p=int(input("Enter the number of sorted element need to be inserted for first array  :"))
print("Enter the elements in array  :")
arr1=[]
for i in range(p):
    arr1.append(int(input()))
q=int(input("Enter the number of sorted element need to be inserted for Second array  :"))
print("Enter the elements in array : ")
array2=[]
for j in range(q):
        array2.append(int(input()))

sol=Solution()
newlist=sol.sortList(arr1,array2,p,q)
print(newlist)

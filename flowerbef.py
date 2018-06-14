def plot(A, N):
        for i, x in enumerate(A):
            if (not x and (i == 0 or A[i - 1] == 0)
                and (i == len(A) - 1 or A[i + 1] == 0)):
                N -= 1
                A[i] = 1
        return N <= 0
    # if(n!=0 and  n<len(flowerbed)):
    #     if(len(flowerbed)>=1 and len(flowerbed)<=20000):
    #         count=0
    #         if (flowerbed[0] == flowerbed[1] == 0):
    #             flowerbed[0] == 1
    #             count += 1
    #         elif (flowerbed[-1] == flowerbed[-1 - 1] == 0):
    #             flowerbed[-1] == 1
    #             count = count + 1
    #         for i in range(1,len(flowerbed)-1):
    #             if(flowerbed[i-1]==flowerbed[i]==flowerbed[i+1]==0):
    #                 if(count<n):
    #                     flowerbed[i]=1
    #                     count+=1
    #
    #         if(n-count==0):return True
    #         else : return False
    #     else:
    #         return False
    # elif(n==0):
    #     count=0
    #     for i in range(0,len(flowerbed),2):
    #         if(flowerbed[i]==1):
    #             count+=1
    #         elif(flowerbed[i]==0):
    #             count=count+1
    #     if(len(flowerbed)%2==1):
    #         l=len(flowerbed)+1
    #         if(count==l/2):
    #             return True
    #     elif(len(flowerbed)%2==0):
    #         l=len(flowerbed)
    #         if(count==l/2):
    #             return True
    # else:
    #     return False


giru=[int(x) for x in input().split()]
k=int(input())
l=plot(giru,k)
print(l)
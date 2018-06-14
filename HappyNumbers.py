def happyNumber(num):
    count=0
    if(len(num)==1):
        z= int(num)
        return int(z*z)
    else:
        for x in range(len(num)):
            y=int(num[x])
            count=count+y*y
    #     if(count==1):
    #     return True
    # else:
    #     z=happyNumber(str(count))
    #





k= input("enter the number you want to find the happy number for: ")
y=happyNumber(k)
print(y)
def square(num,times):
    store=1
    for i in range(1,times+1):
        store=store*num

    return store
x=int(input("Enter the Integer Value need to be reversed : "))
y=square(2,31)
z=square(-2,31)
if(x<y-1 and x>z):
    if(x<0):
        x=abs(x)
        Reverse = 0
        while ( x > 0):
            Reminder = x % 10
            Reverse = (Reverse * 10) + Reminder
            x = x // 10
        if(-Reverse>z):
            print(-Reverse)
        else:
            print("false")
    else:
        Reverse =0
        while (x>0):
            Reminder = x % 10
            Reverse = (Reverse * 10) + Reminder
            x=x//10
        if (Reverse < y-1):
            print(Reverse)
        else:
            print("false")

else:
    print("False")
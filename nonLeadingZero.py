nonleaddigit=int(input("Enter a digit with non leading zero : "))

if(len(nonleaddigit)==1):
        print(nonleaddigit)
else :
nonlead=str(nonleaddigit)
if(nonlead.__contains__(0) and len(nonlead)>1):
        print("! Please Enter a Valid Integet with non leading 0 !")
        goto k
# for i in (range(nonleaddigit)):
#     arr[i]=nonleaddigit[i]

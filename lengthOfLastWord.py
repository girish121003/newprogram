k =input("Enter the string")
if not k or k.isspace():
    print(0)
else:
    j=k.split()
    print(len(j[-1]))
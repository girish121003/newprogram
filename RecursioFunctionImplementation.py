def fact(n): # recursive function to calculate the factorial of a given input
    if n==1:
        return 1
    else:
        j= n*fact(n-1)
        return j


k=int(input("Enter the input")) # getting input from the user
n=fact(k)
print(n)
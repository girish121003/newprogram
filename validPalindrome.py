k=input("Enter the string: ") # input String

L = [',','.',':',';','!','@','#','$','%','^','&','*','(',')','-','_','+','=','[',']','|','"','?','/','~','`','>','<',
     '|',' ',"'","\\"] # list of special character that needs to be eliminated from the input string in order to get the correct palindrome
for x in range(len(L)):
    k=k.replace(L[x],'')# replacing the special character out of input string
temp=''
for y in range(len(k)-1,-1,-1):
    temp+=k[y] # storing the values of string into temp string, reading the input string k from backward
print(temp)

if(temp.lower()==k.lower()): # if both string are same return true
    print("this is a palindrome")
else:
    print("Not a palindrome")


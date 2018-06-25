'''
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the number
equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.
'''


def happynumber(n):
    store=n
    li=[4, 16, 37, 58, 89, 145, 42, 20]# Declared a list of unhappy numbers
    while(store!=1):
        if store in li: # if n occurs in list of unhappy numbers return false
            return False
        else: # we are comuting the number n until we find 1
            store=sum([pow(int(i),2) for i in str(store)])
    return True

k=int(input("Enter the number to find if its happy or not: "))
result=happynumber(k)
print(result)
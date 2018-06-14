def romanToInt(s):
    # dictionary to store roman to integer value
    roman_val= {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    prev_val=0
    current_val=0
    total=0

    for k in range(len(s)-1,-1,-1):
        current_val=roman_val[s[k]] # stores the last value of input string into current_val variable
        if current_val<prev_val: # checks whether current_val is smaller then the previous value if so
                total=total-current_val # deduct current out of total
        else:
                total=total+current_val# else add current into total

        prev_val=current_val # set current to prev_val

    return total 

k=input("Enter the Roman String :")

l=romanToInt(k)

print(l)
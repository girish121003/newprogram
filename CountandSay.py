def countAndSay(n):

    if n <= 1:
        return '1'

    s = countAndSay(n - 1) # used recursion to collect the values from all the counts we have
    if s == '1':
        return '11'
    prev = s[0]
    count = 1
    temp = ''

    for i in range(1, len(s)):# loop started from the strings second position to compare its first element whether it is equal or not
        if prev != s[i]:
            temp += str(count) + prev # if its not equal that means both are different numbers and will be stored in a temporary string starting with count 1 and the number itself
            prev = s[i] # settting the location of current element to previous so that it could be checked with next element
            count = 1 # count stays one since the values are not equal
        else:
            count += 1  # if values are equal then count increases and it could be later added in the string when the current and previous element is not equal
    temp += str(count) + prev
    s = temp
    return s

a= int(input("enter the number to iterate : "))
k=countAndSay(a)
print(k)
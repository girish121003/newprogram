def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    if digits[0] !=0:
        digits=''.join(map(str,digits))
        digits = int(digits)
        digits=digits+1
        l=[]
        for k in str(digits):
            l.append(int(k))

        return l

    elif digits[0] == 0 and len(digits) == 1:
        digits[0] = digits[0] + 1
        return digits
    #for digits in range(len(str(digits[-1]))):
w= [int(x) for x in input().split()]
p=plusOne(w)
print(p)
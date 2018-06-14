def needle(haystack, needle):
    if needle not in haystack:
        return -1
    else:
        m=haystack.find(needle)
        return m








k=input("Enter the String for Haystack")
j= input("Enter Needle")
y=needle(k,j)
print(y)
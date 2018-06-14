def findPattern(pattern,str):
    str = str.split()
    dict = {}
    for k in range(len(pattern)):
        if dict[pattern[k]]==str[k]:
            print("ok")
        elif dict[pattern[k]]!=str[k] and pattern[k] not in dict.keys():
            dict[pattern[k]]=str[k]
        else:
            return False
    return True

a=input("enter the pattern: ")
b=input("enter the string: ")
giru=findPattern(a,b)
print(giru)
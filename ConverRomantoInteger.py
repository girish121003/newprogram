s=input("Enter the Roman number")
map_ = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

if s is None:
    print("Not a correct value")
if len(s) == 0:
    print("Not a correct value")
current_index = 0
res = 0
while (current_index < len(s)):
    if current_index + 1 < len(s):
        if map_[s[current_index]] < map_[s[current_index + 1]]:
            res += map_[s[current_index + 1]] - map_[s[current_index]]
            current_index += 2
        else:
            res += map_[s[current_index]]
            current_index += 1
    else:

        res += map_[s[current_index]]
        current_index += 1

print(res)

# my_dict={}
# my_dict['I']=1
# my_dict['V']=5
# my_dict['X']=10
# my_dict['L']=50
# my_dict['C']=100
# my_dict['D']=500
# my_dict['M']=1000
# my_list=['I','V','X','L','C','D','M']
#
# x=input("Enter the Roman number needs to be converted into Integer")
# count=0
# for z in range(len(x)):
#     if x[z] in my_list :
#        count+=1
#
# if count==len(x):
#
# else:
#     print("kindly enter correct roman number")
#

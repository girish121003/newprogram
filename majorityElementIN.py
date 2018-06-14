lst=[int(x) for x in input().split()]

dict={}
for y in range(len(lst)):

    count = 1
    if lst[y] in dict.keys():
        count=dict[lst[y]]
        dict[lst[y]]=count+1
    else:
        dict[lst[y]]=count

for keys in dict.keys():
    if(dict[keys]>=len(lst)/2):
        print(keys)
k=[int(x) for x in input().split()]
m=0
for x in range(len(k)):
    for y in range(x+1,len(k)):
        if(k[x]>k[y]):
            m=k[x]
            k[x]=k[y]
            k[y]=m

print(k)
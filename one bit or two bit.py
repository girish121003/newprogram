giru=[[1,4],[0,5],[2,6]]
tempall = []
if(len(giru) >1 and len(giru)<10000):
        maxtemp=[]
        mintemp=[]
        countmax=0
        countmin=0
        for i in range(len(giru)):
                maxtemp.append(max(giru[i]))
                countmax+=1
                mintemp.append(min(giru[i]))
                countmin+=1
        k=0
        dict={}
        while(k<len(maxtemp)):

                j=0
                while(j<len(mintemp)):
                    if(k!=j):
                        tempall.append(abs(maxtemp[k]-mintemp[j]))
                        j+=1
                    else:
                        j+=1
                k+=1

print(dict)
#print(max(tempall))
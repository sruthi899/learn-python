countMap={}
x=input('enter the string:')
for i in range(len(x)):
    if countMap.get(x[i],'none')=='none':
        countMap[x[i]]=1
    else:
        countMap[x[i]] += 1
        #print(countMap)
for k, v in countMap.items():
    if v==1:
        print(k,end=" ")

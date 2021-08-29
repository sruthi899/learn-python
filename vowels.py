countMap={}
x=input('enter the string:')
for i in range(len(x)):
   if x[i]=='a' or x[i]=='e' or x[i]=='i' or x[i]=='o' or x[i]=='u':
      if countMap.get(x[i],'none')=='none':
            countMap[x[i]]=1
      else:
            countMap[x[i]]+=1
print(countMap)
for k,v in countMap.items():
        print(k,':',v)



        

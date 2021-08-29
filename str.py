x=(input("enter the string:"))
for i in range(0,len(x)):
    count=0
    for j in range(0,len(x)):
	    if (x[i]==x[j]):
	        count=count+1
    if (count<2):
        print(x[i])
    
countmap = {}
x = (input("string"))
for i in range(len(x)):
    if countmap.get(x[i], 'n') == 'n':
        countmap[x[i]] = 1
    else:
        countmap[x[i]] += 1
for k, v in countmap.items():
    if v==1:
        print(k)


      
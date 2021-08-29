x=(input("enter the string:"))
for i in range(0,len(x)):
    count=0
    for j in range(0,len(x)):
	    if (x[i]==x[j]):
	        count=count+1
    if (count<2):
        print(x[i])
#print('sruthi')	
x=int(input('enter the value:'))
sum=0
if x % 2==0:
    while(x!=0):
	    sum+=(x%10)
	    x=x//10
    print(sum)
else:
    x+=1
	while(x!=0):
	   sum+=(x%10)
	   x=x/10
    print(sum)
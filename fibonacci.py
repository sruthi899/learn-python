n = int(input("enter a number:"))
a, b = 0, 1
count = 0
if n <= 0 :
    print("error")
elif n == 1 :
       print(a)
else:
    while count < n:
        print(a)
        c = a + b
        a = b  
        b = c
        count+=1

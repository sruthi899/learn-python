x = input("enter a string:")
j = -1
flag = 0
for i in x:
    if i == x[j]:
       j = j - 1
       flag = 1
if flag == 1:
    print("string is a palindrom")
else:
    print("is not a palindrom")
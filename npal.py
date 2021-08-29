n = int(input("enter a number:"))
temp = n
r = 0
while n > 0:
    mod = n % 10
    r = r * 10 + mod 
    n = n // 10
if temp == r:
    print('palindrom')
else:
    print('is not a palindrom')

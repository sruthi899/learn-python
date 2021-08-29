a = [1, 2, 3, 4, 5, 6]
b = [5, 6, 7, 8, 9, 20]
c = [0, 0, 0, 0, 0, 0]
for i in range(len(a)):
    #for j in range(len(b)):
    c[i] = a[i] + b[i]
print(c)
def bsearch(arr, n, x):
    L = 0
    U = n-1
    while (L <= U):
        mid = (L + U) // 2
        if arr[mid] == x:
         return mid
        else:
            if arr[mid] > x:
                U = mid
            else:
                L = mid

        return -1






arr= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = len(arr)
x = int(input("enter:"))
r = bsearch(arr, n, x)
if r == -1:
    print("element not present")
else:
    print("found at:", r)


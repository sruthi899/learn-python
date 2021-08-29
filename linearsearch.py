def search(arr, n, x):
    for i in range(0, n):
        if arr[i]== x:
            return i
    return -1
arr = [10, 20, 30, 40, 50, 60]
n = len(arr)
x = int(input("enter the element:"))
r = search(arr, n, x)
if (r == -1):
    print("elemrnt not present")
else:
    print("the index is :", r )


def search(List, n, x):
    for i in range(0, n):
        if List[i] == x:
            return i
    return -1


List = [1, 2, 3, 4, 5]
n = len(List)
x = int(input("enter the element:"))
r = search(List, n, x)
if (r == -1):
    print("element not present")
else:
    print("the index is :", r)

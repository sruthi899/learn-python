arr = [5, 3, 9, 2, 7, 1, 4]
for i in range(len(arr)):

    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("sorted array:")
for i in range (len(arr)):
    print(arr[i])
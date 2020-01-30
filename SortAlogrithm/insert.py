def insert(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range(i-1, -1, -1):
            if temp < arr[j]:
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr


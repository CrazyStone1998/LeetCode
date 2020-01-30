def bubble(arr):
    for i in range(len(arr), 1, -1):
        flag = True
        for j in range(1, i):
            if arr[j] < arr[j - 1]:
                flag = False
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
        if flag:
            return arr
    return arr

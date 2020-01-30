def shell(arr):
    l = len(arr)
    gap = l // 2
    while gap > 0:
        for i in range(gap):
            for j in range(i + gap, l, gap):
                if arr[j] > arr[j-gap]:
                    temp = arr[j]
                    arr[j] = arr[j-gap]
                    arr[j-gap] = temp
        gap //= 2
    return arr

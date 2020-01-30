import time


def select_v1(arr):
    l = len(arr)
    for i in range(l, 1, -1):
        max_num = 0
        max_pos = 0
        min_num = 10000
        min_pos = l
        for j in range(l - i, i):
            if arr[j] > max_num:
                max_num = arr[j]
                max_pos = j
            if arr[j] < min_num:
                min_num = arr[j]
                min_pos = j
        if l - i >= i:
            return arr
        if i - 1 == min_pos and l - i == max_pos:
            arr[i - 1] = max_num
            arr[l - i] = min_num
        elif i - 1 == min_pos:
            arr[max_pos] = arr[l - i]
            arr[i - 1] = max_num
            arr[l - i] = min_num
        elif l - i == max_pos:
            arr[min_pos] = arr[i - 1]
            arr[i - 1] = max_num
            arr[l - i] = min_num
        else:
            arr[max_pos] = arr[i - 1]
            arr[i - 1] = max_num
            arr[min_pos] = arr[l - i]
            arr[l - i] = min_num


def select_v2(arr):
    for i in range(len(arr), 1, -1):
        max = 0
        pos = 0
        for j in range(i):
            if arr[j] > max:
                max = arr[j]
                pos = j
        arr[pos] = arr[i - 1]
        arr[i - 1] = max
    return arr

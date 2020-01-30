def merge(arr, start, end):
    if start < end:
        mid = (start + end) // 2

        merge(arr, start, mid)
        merge(arr, mid + 1, end)

        temp = []
        i = start
        j = mid + 1

        while i < mid + 1 and j < end + 1:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i < mid + 1:
            temp.append(arr[i])
            i += 1
        while j < end + 1:
            temp.append(arr[j])
            j += 1

        for i in temp:
            arr[start] = i
            start += 1

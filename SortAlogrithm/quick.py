def quick_v1(arr, start, end):
    if start < end:
        i, j = start, end
        m = start
        mid = arr[start]
        while i < j:
            while j > i and arr[j] > mid:
                j -= 1
            if j > i:
                arr[m] = arr[j]
                m = j

            while i < j and arr[i] < mid:
                i += 1
            if i < j:
                arr[m] = arr[i]
                m = i

        arr[m] = mid
        quick_v1(arr, start, m - 1)
        quick_v1(arr, m + 1, end)


def quick_v2(arr, start, end):
    if start < end:
        i, j = start, end
        mid = arr[start]
        while i < j:
            while j > i and arr[j] <= mid:
                j -= 1
            while i < j and arr[i] >= mid:
                i += 1
            if i < j:
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
        arr[start] = arr[i]
        arr[i] = mid
        quick_v2(arr, i + 1, end)
        quick_v2(arr, start, i - 1)



def permutations(arr:list, cursor:int):
    if cursor == len(arr)-1:
        print(arr)

    else:
        for i in range(cursor,len(arr)):
            if isRepeat(arr,i):
                continue
            swap(arr,cursor,i)
            permutations(arr,cursor+1)
            swap(arr,cursor,i)

def isRepeat(arr,i):
    return arr[i] in arr[i+1:]

def swap(arr, i , j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

permutations([1,2,3],0)
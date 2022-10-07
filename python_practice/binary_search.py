def binary_search(arr,key,low,high):
    if low <= high:
        mid = low + int((high-low)/2)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr,key,low,mid-1)
        else:
            return binary_search(arr,key,mid+1,high)
    else:
        return -1

arr = [2, 3, 4, 10, 40]
result = binary_search(arr, 10, 0, len(arr)-1)
print(result)

# Program for BINARY SEARCH IN PYTHON

arr = []

# prompt for length

l = int(input("Enter the length of array : "))

# enter array elements one by one

for i in range(1,l+1):
    dummy = input("Enter the list elements one by one: ")
    arr.append(dummy)

# print the given array
print("The given array is ",arr)

# SORT the array using insertion sort
for i in range(1,len(arr)):
    key = arr[i]
    j = i - 1
    # insert the elements where it belongs
    while j >= 0 and key < arr[j] :
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

# Enter the search element

x = input("Enter the search element ")

# seraching for x using binary search

low, high, mid = 0, len(arr) -1, 0

# print(low, high, mid)

while(low <= high):
    mid = (low + high) // 2

    if(arr[mid]<x):
        low = mid + 1

    elif(arr[mid]>x):
        high = mid - 1

    else:
        print("The element is present at the index ",mid)
        break


if (low>high):
    print("The element is not present")


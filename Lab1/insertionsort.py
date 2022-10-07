# Program for INSERTION sort IN PYTHON

# driver

arr = []

# prompt for length

l = int(input("Enter the length of array : "))

# enter array elements one by one

for i in range(1,l+1):
    dummy = input("Enter the list elements one by one: ")
    arr.append(dummy)


# print the given array
print("The given array is ",arr)

# insertion sort

for i in range(1,len(arr)):
    key = arr[i]
    j = i - 1
    # insert the elements where it belongs
    while j >= 0 and key < arr[j] :
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

# print array
print("The sorted array : ",arr)
            
    





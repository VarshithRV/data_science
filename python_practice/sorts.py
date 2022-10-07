# insertion, bubble and selection sorting algorithms :

def insertion_sort(arr): # insertion sort
    for i in range(len(arr)):
        j = i-1
        key = arr[i]
        while(j>=0 and key < arr[j]):
            arr[j+1],arr[j] = arr[j],arr[j+1]
            j -= 1
        #arr[j+1] = key
    return arr

def selection_sort(arr): # selection sort
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if(arr[min_index]>arr[j]):
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]
        print(arr)
    return arr
    
def bubble_sort(arr): # bubble sort
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr

        
# main function
if __name__ == "__main__":
    arr = [2,4,1,5,8]
    arr = bubble_sort(arr)
    print(arr)

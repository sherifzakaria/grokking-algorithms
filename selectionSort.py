def findSamllest(arr):
    """
    return index of smallest element in an array
    """

    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selectionSort(arr):
    """
    sort elements in an array using selection sort
    """
    newArr = []
    smallest = arr[0]

    for i in range(len(arr)):
        smallest = findSamllest(arr)  
        newArr.append(arr.pop(smallest))
    
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
print(selectionSort([85, 35, 698, 29, 180]))
print(selectionSort([655, 3189, 876, 26, 810]))

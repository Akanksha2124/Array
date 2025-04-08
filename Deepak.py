def move_negatives(arr):
    j = 0  

    for i in range(len(arr)):
        if arr[i] < 0:
           
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr


arr = [4, -1, 9, -3, -5, 2, -7, 6]
print("Original array:", arr)
result = move_negatives(arr)
print("After moving negatives to one side:", result)

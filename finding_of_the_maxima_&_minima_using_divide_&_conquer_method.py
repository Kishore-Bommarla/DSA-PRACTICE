def FindMaximaAndMinima(arr, i, j):
    if i == j:
        # Only one element
        min_value = arr[i]
        max_value = arr[i]
    elif i == j - 1:
        # Two elements
        if arr[i] < arr[j]:
            max_value = arr[j]
            min_value = arr[i]
        else:
            max_value = arr[i]
            min_value = arr[j]
    else:
        mid = i + (j - i) // 2
        max_1, min_1 = FindMaximaAndMinima(arr, i, mid)
        max_2, min_2 = FindMaximaAndMinima(arr, mid + 1, j)
        
        if max_1 < max_2:
            max_value = max_2
        else:
            max_value = max_1
        
        if min_1 > min_2:
            min_value = min_2
        else:
            min_value = min_1
    
    return max_value, min_value

arr = [20, 39, 45, 65, 21, 44, 89, 92]
i = 0
j = len(arr) - 1
max_value, min_value = FindMaximaAndMinima(arr, i, j)
print(max_value, min_value)

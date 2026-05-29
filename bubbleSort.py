def binarySearch(arr : list)->list:
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
        
        
nums = [1,3,2,5,7]

print(binarySearch(nums))
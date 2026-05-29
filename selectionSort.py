

def find_kth_smallest(arr : list[int], k:int)->int:
    
    
    for i in range(len(arr)):
        min_index = i
        
        for j in range(i + 1, len(arr)):
            
            if arr[i] > arr[j]:
                min_index = arr[j]
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    print(arr)
        
    return arr[k-1]


numbers = [1,3,2,4,5]

print(find_kth_smallest(numbers, 3))
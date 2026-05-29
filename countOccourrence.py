

def count_occourrence(arr, target):
    count = 0
    
    for index, item in enumerate(arr):
        if arr[index] == target:
            count += 1
            
    return count

numbers = [1,5,3,5,2,5]
print(count_occourrence(numbers, 5))

nums = [1,2,4,6,7]



def binarySearch(nums, target):
    
    left = 0
    right = len(nums)-1
    mid = (left + right)//2
    
    while left <= right:
        
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            left = mid + 1
        else:
            
            right = mid - 1
        mid = (left + right)//2
        
        
        if target not in nums:
            if target > nums[right]:
                return right + 1
            if target > nums[left]:
                return left + 1
            else:
                left = 0
            
        
        return left
    
print(binarySearch(nums, 1))
numbers = [1,2,3,4,5] # num1 + num2 = 9




def two_sum_brute_force(nums):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + numbers[j] == 9:
                return [nums[i], nums[j]]
            


def two_sum(nums, target):
    result = {}
    
    for index, num in enumerate(numbers):
        x = target - num
        
    
        
        if x in result:
            print(result)
            print(x)
            return [result[x], index]
        result[num] = index


result = two_sum(numbers, 9)
print(result)
        
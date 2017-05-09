import test_sort

def insertion_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    
    for i in range(1,n):
        temp = nums[i]
        for j in range(0, i):
            if temp < nums[j]:
                nums[j], temp = temp, nums[j]
        nums[i] = temp
        
    return


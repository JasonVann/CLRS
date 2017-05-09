from test_sort import * 

def insertion_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    
    for i in range(1,n):
        # Warning: starting from i = 1 causes too many unnecessary comparisons
        temp = nums[i]
        for j in range(0, i):
            if temp < nums[j]:
                nums[j], temp = temp, nums[j]
        nums[i] = temp
        
    return

def insertion_sort_clrs(nums):
    n = len(nums)
    for j in range(1, n):
        key = nums[j]
        i = j - 1
        while i >= 0 and nums[i] > key:
            nums[i+1] = nums[i]
            i = i - 1
        nums[i+1] = key

data = gen_test(1e4)

print("Pre-sort: ",verify_sort(data))
insertion_sort(data)
print("Sort1 finished.")
print("Sort1 success:",verify_sort(data))

random.shuffle(data)
insertion_sort_clrs(data)
print("Sort 2 success:",verify_sort(data))
            

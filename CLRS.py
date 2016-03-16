# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:04:48 2016

For 6.006 MIT Algorithm I
@author: jasonniu
"""
import time
import random

sorted_data = []

#A1
def insertion_sort(nums):
    # why not O(n^3)?
    global sorted_data
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[j] < nums[i]:
                # Add j before i
                temp = nums[j]
                nums.pop(j)         #O(n)
                nums.insert(i, temp) # O(n)
    sorted_data = nums
    return nums

def insertion_sort_clrs(A, asc = True):
    global sorted_data
    for j in range(1, len(A)):
        key = A[j]
        # insert A[j] to the sorted sequence A[0..j-1]
        i = j -1
        while i >= 0 and ((asc and A[i] > key) or (not asc and A[i] < key)):
            A[i + 1] = A[i]
            i = i -1
        A[i + 1] = key
    #print A
    sorted_data = A
    print A[:30]
    print sorted_data[:30]
    return A
    
def test_list_insert(data):
    i = random.randint(1, len(data))
    num = random.randint(1, len(data))
    data.insert(i, num)
    return data
    
def test_list_pop(data):
    i = random.randint(1, len(data))
    #num = random.randint(1, len(data))
    data.pop(i)
    return data
    
def benchmark(func, n, asc = True):
    # benchmark and validate
    #n = 1E4
    lo = 1
    hi = 10000
    data = stress_test_prep(int(n), lo, hi)
    
    #print data[:20]
    start = time.time()
    
    nums = func(data, asc)
    
    end = time.time()
    print 'Count: ', len(nums)
    print 'Func execution time: ', (end - start)
    validate_sort(sorted_data, asc)
  

def stress_test_prep(n, lo, hi):
    data = []
    random.seed(1)
    
    for i in range(int(n)):
        a = random.randint(lo, hi)
        #b = random.randint(a, hi)
        #temp = (a, b)
        #print temp
        data.append(a)
    return data
    
def validate_sort(data, asc):
    for i in range(1, len(data) - 1):
        if (asc and data[i] > data[i + 1]) or (not asc and data[i] < data[i + 1]):
            print "Sorting failed: ", i, data[i], data[i + 1]
            break
    print 'Sorting succeeds: ', len(data)
    
nums = [5,2,4,6,1,3]
#insertion_sort_clrs(nums)

'''
Me: 
100: 0.0006
1000: 0.044
1E4: 4.3s

clrs: ?? O(n)
100: 0.00005s
1000: 0.04s
1E4: 4.46s

Python list insert
1E5: 0.00014
1E6: 0.00132
1E7: 0.007

Python list pop
1E6: 0.002
1E7: 0.0045

'''


    
n = 1E3
#print insertion_sort(nums)

#benchmark(insertion_sort, n)
benchmark(insertion_sort_clrs, n, asc = False)
#benchmark(test_list_insert, n)
#benchmark(test_list_pop, n)

#print insertion_sort_clrs(nums)


# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:04:48 2016

For 6.006 MIT Algorithm I
@author: jasonniu
"""
import time
import random
import sys

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
    
    #print data
    start = time.time()
    
    #nums = func(data, asc)
    # For merge sort:
    nums = func(data, 0, len(data) - 1)
    
    end = time.time()
    print 'Count: ', len(nums)
    print 'Func execution time: ', (end - start)
    #print nums
    validate_sort(nums, asc)
  

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
            return
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

def combine_inversion(A1, A2, asc, count):
    # A1, A2 are all sorted
    # O(n)
    sorted_A = []
    if(len(A1) > len(A2)):
        big = A1
        small = A2
    else:
        big = A2
        small = A1
    i = 0
    j = 0
    while True:
        #print i, j, sorted_A
        if j == len(big):
            sorted_A.extend(small[i:])
            break
        elif i == len(small):
            #print 'b', sorted_A, j, big[j:]
            sorted_A.extend(big[j:])
            break
        #print i, j, small[i], big[j], sorted_A        
        if(small[i] > big[j]):
            count += len(A1[i : ])
            sorted_A.append(big[j])
            j += 1
        else:
            sorted_A.append(small[i])
            i += 1
            
    #sorted_A.extend(big[len(small):])
    return count
   
#print combine_inversion([5, 9], [4,7], True, 0)

def combine(A1, A2, asc):
    # A1, A2 are all sorted
    # O(n)
    sorted_A = []
    if(len(A1) > len(A2)):
        big = A1
        small = A2
    else:
        big = A2
        small = A1
    i = 0
    j = 0
    while True:
        #print i, j, sorted_A
        if j == len(big):
            sorted_A.extend(small[i:])
            break
        elif i == len(small):
            #print 'b', sorted_A, j, big[j:]
            sorted_A.extend(big[j:])
            break
        #print i, j, small[i], big[j], sorted_A        
        if(small[i] > big[j]):
            sorted_A.append(big[j])
            j += 1
        else:
            sorted_A.append(small[i])
            i += 1
            
    #sorted_A.extend(big[len(small):])
    return sorted_A
   
def merge_sort(A, asc = True):
    # 2.3.1
    n = len(A)
    if n == 1:
        return A
    elif n == 2:
        if A[0] > A[1]:
            temp = []
            temp.append(A[1])
            temp.append(A[0])
            return temp
        else:
            return A
            
    A1 = A[:n/2]
    A2 = A[n/2:]
    
    C = merge_sort(A1, asc)
    D = merge_sort(A2, asc)
    E = combine(C, D, asc)    
    #print 'merged:', C, D, E
    '''
    print A1
    merge_sort(A1, asc)
    merge_sort(A2, asc)
    print A1
    A = combine(A1, A2, asc)
    '''
    return E

import math

def merge_sort_insertion(A, p, r):
    # r: index of last item
    # switch to insertion sort on small arrays
    k = int(math.log(len(A), 2))
    #print k
    if p < r:
        q = (p+r)/2
        #print 'a', p, q, r
        if r - p < k:
            A[p: r + 1] = insertion_sort(A[p: r + 1])
        else:
            merge_sort_insertion(A, p, q)
            merge_sort_insertion(A, q + 1, r)
            merge_clrs(A, p, q, r)
    return A
    

A = [5, 6, 3, 5, 7, 9, -1, 8, 4]
A1 = [1344, 8475, 7638, 2551, 4955, 4495, 6516, 7888, 939, 284, 8358]
A1 = [2,3,8,6,1]

#print merge_sort_insertion(A1, 0, len(A1) - 1)

n = 1e2
#benchmark(merge_sort_insertion, n)


def merge_sort_clrs_inversion(A, p, r):
    # r: index of last item
    count = 0
    if p < r:
        q = (p+r)/2
        #print 'a', p, q, r
        count = count + merge_sort_clrs_inversion(A, p, q)
        count = count + merge_sort_clrs_inversion(A, q + 1, r)
        count = count + merge_clrs_inversion(A, p, q, r)
    return count
    
def merge_clrs_inversion(A, p, q, r):
    #n1 = q - p + 1
    #n2 = r - q
    L = A[ p : q + 1]
    R = A[q + 1: r + 1]
    L.append(sys.maxint) # Sentinel
    R.append(sys.maxint)
    #print 'b', p, q, r, L, R, A
    i = 0
    j = 0
    #print 'l', L
    count = 0
    #print 'a', count
    for k in range(p, r + 1):
        #print 'c', k, L[i], R[j], i, j
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            if (L[i] != sys.maxint):
                #print q, p, count, L
                count += q + 1 - p - i 
                print A[p + i: q + 1], L[i], R[j], L, R
                
            A[k] = R[j]
            j += 1
    print 'b', count
    return count

print merge_sort_clrs_inversion(A1, 0, len(A1) - 1)


def merge_sort_clrs(A, p, r):
    # r: index of last item
    if p < r:
        q = (p+r)/2
        #print 'a', p, q, r
        merge_sort_clrs(A, p, q)
        merge_sort_clrs(A, q + 1, r)
        merge_clrs(A, p, q, r)
    return A
    
def merge_clrs(A, p, q, r):
    #n1 = q - p + 1
    #n2 = r - q
    L = A[ p : q + 1]
    R = A[q + 1: r + 1]
    L.append(sys.maxint) # Sentinel
    R.append(sys.maxint)
    #print 'b', p, q, r, L, R, A
    i = 0
    j = 0
    for k in range(p, r + 1):
        #print 'c', k, L[i], R[j], i, j
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    #return A
         
def f_b(A):
    A.append(99)
    
def f_a():
    A = [1,2]
    f_b(A)
    print A
    
#f_a()
        
A1 = [5]
A2 = [6,7]
#print A1, A2
#print combine(A1, A2)

#print merge_clrs([5, 6, 1, 4], 0, 2, 3)



#merge_sort_clrs([])

A = [5, 2, 4, 7, 1, 3, 2, 6]
#print merge_sort_clrs(A, 0, 7)
    
n = 1E3
#benchmark(merge_sort_insertion, n)

'''
Merge Sort
1E3: 0.004
1E4: 0.06
1E5: 0.77
1E6: 9.2s

clrs:
1E6: 7.1s

Merge sort with insertion sort
1E4: 0.04
1E5:0.5
1E6: 6.28s

'''

#print insertion_sort(nums)

#benchmark(insertion_sort, n)
#benchmark(insertion_sort_clrs, n, asc = False)

#benchmark(test_list_insert, n)
#benchmark(test_list_pop, n)

#print insertion_sort_clrs(nums)

#benchmark(merge_sort, n)

#benchmark(merge_sort_clrs, n)

def bubble_sort(A, asc = True):
    # sort asc
    n = len(A)
    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if A[j] < A[j-1] and asc:
                temp = A[j - 1]
                A[j - 1] = A[j]
                A[j] = temp
            elif A[j] > A[j-1] and not asc:
                temp = A[j - 1]
                A[j - 1] = A[j]
                A[j] = temp
                
    return A
    
A = [2,3,1,0,18,11]
#print bubble_sort(A, False)

n = 1E2

'''
Bubble Sort
1E3: 0.11s
1E4: 12s


'''
#benchmark(bubble_sort, n)


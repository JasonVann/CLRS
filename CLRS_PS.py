# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:17:23 2016

@author: jasonniu
#CLRS Exercises and PS
"""

# Ex2.1-3
def linear_search(data, num):
    # Ex2.1-3
    for i in range(len(data)):
        if num == data[i]:
            print 'Found it! ', i, data[i]
            return i
    print 'Not found'
    return None
    
# Ex2.1-4
def add_binary_list(a, b):
    # a, b are binary int in arrays
    # list: pass by reference
    if len(a) > len(b):
        big = a[:]
        small = b[:]
    else:
        big = b[:]
        small = a[:]
    
    #c = big[:]
    c = [0 for x in range(len(big))]
    c.insert(0, 0)
    
    for i in range(-1, -len(big) - 1, -1):
        if(i < - len(small)):
            temp_s = 0
        else:
            temp_s = int(small[i])
        temp_b = int(big[i])
        print i, temp_s, temp_b
        print big, small, c
        temp_sum = temp_s + temp_b + c[i]
        if temp_sum >= 2:
            # should be between 0 and 3
            c[i] = (temp_sum) % 2
            #big[i - 1] = int(big[i - 1]) + (temp_s + temp_b)/2
            c[i - 1] = int(c[i - 1]) + (temp_sum)/2
        else:
            c[i] = temp_sum
        print big, small, c
    print a, b, c
    return c
    
def verify_add_binary_list(a, b, c):
    A = ''
    B = ''
    C = ''
    for i in a:
        A += str(i)
    for i in b:
        B += str(i)
    for i in c:
        C += str(i)
    A = int(A, 2)
    B = int(B, 2)
    C = int(C, 2)
    print A, B, C
    assert A + B == C, 'Not Equal'
    
def Test_Ex214():
    a = [1,0,0,0]
    b = [1,1,0, 1,1,1, 0]
    c = add_binary_list(a, b)
    
    verify_add_binary_list(a, b, c)

#Test_Ex214()

# Ex2.3-4
# T(n) = T(n-1) + n
# => O(n^2)

# Ex2.3-5
def binary_search(data, lo, hi, a):
    if lo > hi:
        return 'Not found'
    elif lo == hi and data[lo] != a:
        return 'Not found'
    mid = lo + (hi - lo)/2
    if data[mid] > a:
        return binary_search(data, lo, mid - 1, a)
    elif data[mid] == a:
        return mid
    else:
        return binary_search(data, mid + 1, hi, a)
        
#print binary_search([1,2,3,6,7], 0, 4, 1)

# PS 2-3
# a. O(n)
# b. O(n^2)

'''PS 2-4
a. (2, 1), (3, 1), (8, 1), (6, 1), (8, 6)
b. sorted desc,  (n - 1) + (n - 2) +... 1 -> n*(n-1)/2


'''

import sys

# Ex4.1-2
def max_subarray_brute_force(A, lo = None, hi = None):
    # find the max sub array by brute-force method
    res = []
    global_max = -sys.maxint
    global_max_idx = -sys.maxint
    if lo == None:
        lo = 0
    if hi == None:
        hi = len(A) - 1

    #print lo, hi
    for i in range(lo, hi + 1):
        temp = []
        temp_sum = 0
        max_sum = -sys.maxint
        for j in range(i, hi + 1):
            temp_sum += A[j]
            if temp_sum > max_sum:
                max_sum = temp_sum
                temp = [i, j, max_sum]
        res.append(temp)
        if temp[2] > global_max:
            global_max_idx = i - lo
            global_max = temp[2]

    #print res, global_max_idx
    #print res[global_max_idx]
    return res[global_max_idx]

def find_max_crossing_subarray(A, low, mid, high):
    # C4.1
    # high: index of last element
    # treat mid in the left section
    #print low, mid, high
    max_sum_r = -sys.maxint
    max_sum_l = -sys.maxint
    max_r_idx = 0
    max_l_idx = 0
    temp_sum_r = 0
    temp_sum_l = 0
    for i in range(mid + 1, high + 1):
        if temp_sum_r + A[i] > max_sum_r:
            max_r_idx = i
            max_sum_r = temp_sum_r + A[i]
        temp_sum_r += A[i]
    # Then left
    #if mid - low > 0:
    for i in range(mid, low - 1, -1):
        if temp_sum_l + A[i] > max_sum_l:
            max_l_idx = i
            max_sum_l = temp_sum_l + A[i]
        temp_sum_l += A[i]
    max_sum = max_sum_r + max_sum_l
    #print 'r', mid, high, max_r_idx, max_sum_r, A[max_r_idx]
    #print 'l', mid, low, max_l_idx, max_sum_l, A[max_l_idx]

    result = [max_l_idx, max_r_idx, max_sum]
    return result
    
def max_sub_array(A, p, r):
    # r: index of last item
    if p == r:
        return [p, r, A[p]]
    if p < r:
        q = (p + r)/2
        #print 'a', p, q, r
        [l1, r1, max_sum1] =  max_sub_array(A, p, q)
        [l2, r2, max_sum2] = max_sub_array(A, q + 1, r)
        [l3, r3, max_sum3] = find_max_crossing_subarray(A, p, q, r)
        #print 'compare:', p, q, r, 'val:', max_sum1, max_sum2, max_sum3
        if max_sum3 >= max_sum1 and max_sum3 >= max_sum2:
            return [l3, r3, max_sum3]
        elif max_sum2 >= max_sum3 and max_sum2 >= max_sum1:
            return [l2, r2, max_sum2]
        else:
            return [l1, r1, max_sum1]
    return 'Not found'
    
def max_sub_array_mixed(A, p, r):
    # r: index of last item
    if p == r:
        return [p, r, A[p]]
    if r - p < 20:
            #print A, p, r
            return  max_subarray_brute_force(A, p, r)
            
    if p < r:
        q = (p + r)/2
        #print 'a', p, q, r
                    
        [l1, r1, max_sum1] =  max_sub_array_mixed(A, p, q)
        [l2, r2, max_sum2] = max_sub_array_mixed(A, q + 1, r)
        [l3, r3, max_sum3] = find_max_crossing_subarray(A, p, q, r)
        #print 'compare:', p, q, r, 'val:', max_sum1, max_sum2, max_sum3
        if max_sum3 >= max_sum1 and max_sum3 >= max_sum2:
            return [l3, r3, max_sum3]
        elif max_sum2 >= max_sum3 and max_sum2 >= max_sum1:
            return [l2, r2, max_sum2]
        else:
            return [l1, r1, max_sum1]
    return 'Not found'
    
def benchmark(func, n, rep = 1, asc = True):
    # benchmark and validate
    #n = 1E4
    lo = 1
    hi = 10000
    total_t = 0
    i = 0
    while i < rep:
        data = stress_test_prep(int(n), lo, hi)
        
        #print data
        start = time.time()
        
        #nums = func(data, asc)
        # For merge sort:
        nums = func(data, 0, len(data) - 1)
        
        end = time.time()
        total_t += end - start
        i += 1
        
    print 'result: ', nums
    print 'Func execution time: ', total_t/float(rep)
    #print nums
    #validate_sort(nums, asc)
  

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
    
A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7, 3, 7, 5, 3, 9, 11]
#A = [0]
#A = [13, 1, -2]
#print max_subarray_brute_force(A, 0, len(A) - 1)
#print max_sub_array(A, 0, len(A) - 1)
#print max_sub_array_mixed(A, 0, len(A) - 1)
#print max_subarray_brute_force(A, 11,21)

def Ex413():
    n = 1e3
    rep = 1
    #benchmark(max_subarray_brute_force, n, rep)
    
    #benchmark(max_sub_array, n, rep)
    #benchmark(max_sub_array_mixed, n, rep)
    benchmark(max_subarray_linear, n, rep)
    
    sol =  '''
    n = 15, 4.2e-5s VS 4.5e-5s
    n = 16, 4.6e-5s VS 5e-5s
    Crossover point is about 16 to 20
    
    When n is large, > 1000 or so, mixed version is about 10% faster
    '''
    print sol

#Ex413()

def max_subarray_linear(A, i, j):
    '''
    First find the sum up to index k for every k
    Then out of the max(sums), the max subarray is either the sums[j], or A[i..j+1]
    '''
    temp_max = -sys.maxint
    s = 0
    temp_i = j
    sums = []
    temp_sum = 0
    for k in range(0, len(A) - 1):
        temp_sum += A[k]
        sums.append(temp_sum)
    
    temp_max = max(sums)
    j = sums.index(temp_max)
    
    #print sums, temp_max, j
    
    for k in range(j + 1, -1, -1):
        s += A[k]
        if s >= temp_max:
            temp_max = s
            temp_i = k
    
    #print temp_i, j + 1, temp_max
    #print A[temp_i : j + 1]
    return [temp_i, j + 1, temp_max]
    
def Ex415():
    '''
    1e7: 3.4s
    '''
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7, 3, 7, 5, 3, 9, 11]
    max_subarray_linear(A, 0, len(A) - 1)
    #benchmark(max_subarray_linear, n, rep)

Ex415()
   
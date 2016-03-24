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
        
print binary_search([1,2,3,6,7], 0, 4, 1)

# PS 2-3
# a. O(n)
# b. O(n^2)

'''PS 2-4
a. (2, 1), (3, 1), (8, 1), (6, 1), (8, 6)
b. sorted desc,  (n - 1) + (n - 2) +... 1 -> n*(n-1)/2


'''

import sys

# Ex4.1-2
def max_subarray_brute_force(A):
    # find the max sub array by brute-force method
    res = []
    global_max = -sys.maxint
    global_max_idx = -sys.maxint
    for i in range(len(A)):
        temp = []
        temp_sum = 0
        max_sum = -sys.maxint
        for j in range(i, len(A)):
            temp_sum += A[j]
            if temp_sum > max_sum:
                max_sum = temp_sum
                temp = [max_sum, i, j]
        res.append(temp)
        if temp[0] > global_max:
            global_max_idx = i
            global_max = temp[0]

    print res
    print res[global_max_idx]
    return res[global_max_idx][0]

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
#A = [0]
#A = [13, 1, -2]
print max_subarray_brutal_force(A)
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
inv

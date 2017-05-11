# Ex2.3-5
from merge_sort import *

def binary_search_recur(A, x, l, r):
    # Try to find x in sorted list A recursively
    # Return the index of x if found, return False otherwise
    if l > r:
        return False
    mid = int(l + (r-l)/2)
    if A[mid] < x:
        return binary_search_recur(A, x, mid+1, r)
    elif A[mid] == x:
        return mid
    else:
        return binary_search_recur(A, x, l, mid-1)

def one_test(n = 1000):
    # Generate a single test for binary search
    max_num = 2e3
    A = gen_test(n, max_num)
    merge_sort(A, 0, n-1)
    a = random.randint(-max_num, max_num)
    idx = binary_search_recur(A, a, 0, n-1)
    #print(a, idx)
    if not idx and a not in A:
        #print("Not found and correct")
        return True
    elif A[idx] == a:
        #print("Found!")
        return True
    else:
        #print("Something went wrong!")
        return False

def many_tests(count = 10):
    # Repeated calls one_test to verify binary search
    list_len = 1000
    for i in range(count):
        res = one_test(list_len)
        if not res:
            print("Test failed")
            return
    print("Test passed!" )
        

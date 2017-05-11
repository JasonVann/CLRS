# PS2-2
from test_sort import *

def bubble_sort(A):
    # My implementation of bubble sort
    # Keeps swapping two adjacent items if they are out-of-order
    # After one iteration of the inner loop, the largest i-th item wil be in its final position
    n = len(A)
    for i in range(n):
        for j in range(n-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]

def bubble_sort_op(A):
    # An optimized version of bubble sort
    # Avoid looking at the last i items in the inner loop as those items should be in order
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1, 1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                
def test(n=1000):
    A = gen_test(n)
    bubble_sort2(A)
    print(verify_sort(A))
    


                
                
            


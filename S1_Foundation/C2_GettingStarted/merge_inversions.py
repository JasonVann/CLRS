# CLRS PS2-4
from test_sort import *

def count_inversions(A, p, r):
    # Count # of inversions in a list with the merge-sort method
    # An inversion occurs if A[i] > A[j] and i < j
    inversions = 0
    if p < r:
        q = int(p + (r-p)/2)
        inversions += count_inversions(A, p, q)
        inversions += count_inversions(A, q+1, r)
        inversions += merge_inversions(A, p, q, r)
    return inversions

def merge_inversions(A, p, q, r):
    # Count the # of inversions when merging L and R
    # Use sentinel items to get rid of checking leftover items from L or R
    import sys
    n1 = q - p + 1
    n2 = r - q
    # Create new list to hold A[p...q]
    L = A[p:q+1]
    R = A[q+1:r+1]
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = 0
    j = 0
    inversions = 0
    counted = False
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            inversions = inversions + n1 - i
            A[k] = R[j]
            j += 1
    return inversions

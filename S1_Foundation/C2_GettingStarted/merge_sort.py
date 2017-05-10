from test_sort import *

def merge(A, p, q, r):
    # Assumes A[p..q], A[q+1...r] are already sorted
    n1 = q - p + 1
    n2 = r - q
    
    out = [0]*(n1+n2)
    i = p
    j = q + 1
    k = 0
    while i <= q and j <= r:
        #print(i, j, A[i], A[j], out, k)
        if A[i] <= A[j]:
            out[k] = A[i]
            i += 1
        else:
            out[k] = A[j]
            j += 1
        k += 1
    #print(out, i, j, k)
    if i <= q:
        for i2 in range(i, q+1):
            out[k] = A[i2]
            k += 1
    elif j <= r:
        for j2 in range(j, r+1):
            out[k] = A[j2]
            k += 1
    # Copy back the sorted arry to original array
    for i in range(p, r+1):
        A[i] = out[i-p]
    #print(A)

def merge_clrs(A, p, q, r):
    # Use sentinel items to get rid of checking leftover items from L or R
    pass

def merge_sort(A, p, r):
    # A[p] is the left-most item we are interested in
    # A[r] is the right-most item
    n = r - p + 1
    if n <= 1:
        return 
    elif n == 2:
        if A[p] > A[r]:
            A[p], A[r] = A[r], A[p]
        return
    mid = p + int((r-p)/2) # In python3, may be float so cast to int
    merge_sort(A, p, mid)
    merge_sort(A, mid+1, r)
    merge(A, p, mid, r)
    return
        
def test_merge():
    A = [9,1,3,5,7,9,11,13,2,4,6,8,10]
    merge(A, 1, 7, 12)

def test_merge_sort(n = 1000):
    data = gen_test(n)
    merge_sort(data, 0, n-1)
    print(verify_sort(data))

    

# Implemented as in CLRS 6.2

import Heap

def max_heapify(A:Heap, i):
    '''
    Maintains the max heap property: A[i] >= A[left(i)] && A[i] >= A[right(i)]
    '''
    if i >= A.size or i < 0:
        raise "i is not a valid index"

    left = A.left(i)
    right = A.right(i)
    largest = i
    if left is not None and A.data[left] >= A.data[i]:
        largest = left
    if right is not None and A.data[right] >= A.data[largest]:
        largest = right
    if i != largest:
        # Then max heap property is violated
        A.data[largest], A.data[i] = A.data[i], A.data[largest]
        max_heapify(A, largest)

def max_heapify_recur(A:Heap, i):
    '''
    A recursive version of max_heapify
    For Ex6.2-5
    '''
    if i >= A.size or i < 0:
        raise "i is not a valid index"

    while i < A.size:
        left = A.left(i)
        right = A.right(i)
        largest = i
        if left is not None and A.data[left] >= A.data[i]:
            largest = left
        if right is not None and A.data[right] >= A.data[largest]:
            largest = right
        if i != largest:
            # Then max heap property is violated
            A.data[largest], A.data[i] = A.data[i], A.data[largest]
            i = largest
        else:
            break

def test_max_heapify():
    A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    heap = Heap.Heap(A)
    print(heap.data)
    max_heapify(heap, 1)
    print(heap.data)

#test_max_heapify()

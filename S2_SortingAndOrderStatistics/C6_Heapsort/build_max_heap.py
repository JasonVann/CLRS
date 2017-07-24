from max_heapify import *
import math

def build_max_heap(A:Heap):
    max_internal_idx = math.ceil(A.size/2)
    for i in range(max_internal_idx, -1, -1):
        max_heapify_recur(A, i)

def test_build_max_heap():
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap = Heap.Heap(A)
    print(heap.data)
    build_max_heap(heap)
    print(heap.data)

#test_build_max_heap()
